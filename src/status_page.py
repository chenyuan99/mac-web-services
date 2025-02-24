from flask import Flask, render_template, jsonify
from datetime import datetime
import os
import requests
import time
import psutil
import subprocess
import json
import re
import pytz
from collections import deque
import threading
import traceback
import sys

app = Flask(__name__)

# Services to monitor
SERVICES = {
    'Ollama': 'http://localhost:11434/api/tags',  # Ollama API endpoint
}

# Store last 1000 log lines in memory
LOG_BUFFER = deque(maxlen=1000)

def get_mac_gpu_info():
    try:
        # Get GPU name and type
        gpu_cmd = "system_profiler SPDisplaysDataType -json"
        gpu_output = subprocess.check_output(gpu_cmd, shell=True)
        gpu_data = json.loads(gpu_output)
        
        gpu_info = []
        for gpu in gpu_data.get('SPDisplaysDataType', []):
            gpu_name = gpu.get('sppci_model', 'Unknown GPU')
            
            # Get GPU utilization using powermetrics
            # Note: requires sudo, so we'll skip it for now
            # Could be implemented with proper permissions
            
            # Get memory information from ioreg for built-in GPU
            if 'Intel' in gpu_name or 'Apple' in gpu_name:
                ioreg_cmd = "ioreg -l | grep -i 'IOGPUMemorySize\|IOGPUFreeMemory'"
                try:
                    ioreg_output = subprocess.check_output(ioreg_cmd, shell=True).decode()
                    
                    # Extract memory values
                    total_memory = re.search(r'IOGPUMemorySize.*?= (\d+)', ioreg_output)
                    free_memory = re.search(r'IOGPUFreeMemory.*?= (\d+)', ioreg_output)
                    
                    if total_memory and free_memory:
                        total_mb = int(total_memory.group(1)) / (1024 * 1024)
                        free_mb = int(free_memory.group(1)) / (1024 * 1024)
                        used_mb = total_mb - free_mb
                        
                        gpu_info.append({
                            'name': gpu_name,
                            'memory_total': f"{total_mb:.0f}MB",
                            'memory_used': f"{used_mb:.0f}MB",
                            'memory_free': f"{free_mb:.0f}MB",
                            'memory_percent': f"{(used_mb/total_mb*100):.1f}%"
                        })
                    else:
                        gpu_info.append({
                            'name': gpu_name,
                            'memory_total': 'N/A',
                            'memory_used': 'N/A',
                            'memory_free': 'N/A',
                            'memory_percent': 'N/A'
                        })
                except subprocess.CalledProcessError:
                    gpu_info.append({
                        'name': gpu_name,
                        'memory_total': 'N/A',
                        'memory_used': 'N/A',
                        'memory_free': 'N/A',
                        'memory_percent': 'N/A'
                    })
            else:
                # For discrete GPUs, just show the name
                gpu_info.append({
                    'name': gpu_name,
                    'memory_total': 'N/A',
                    'memory_used': 'N/A',
                    'memory_free': 'N/A',
                    'memory_percent': 'N/A'
                })
        
        return gpu_info
    except Exception as e:
        print(f"Error getting GPU info: {e}")
        return []

def get_server_time():
    local_tz = datetime.now().astimezone().tzinfo
    current_time = datetime.now(local_tz)
    return {
        'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
        'timezone': str(local_tz),
        'timestamp': int(current_time.timestamp()),
        'timezone_offset': current_time.strftime('%z')
    }

def get_system_metrics():
    # CPU info
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Memory info
    memory = psutil.virtual_memory()
    memory_total = f"{memory.total / (1024 ** 3):.1f}GB"
    memory_used = f"{memory.used / (1024 ** 3):.1f}GB"
    memory_percent = memory.percent
    
    # GPU info
    gpu_info = get_mac_gpu_info()
    
    # Server time info
    server_time = get_server_time()
    
    return {
        'status': 'operational',
        'latency': 'N/A',
        'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'details': {
            'cpu': {
                'usage': f"{cpu_percent}%",
                'cores': cpu_count
            },
            'memory': {
                'total': memory_total,
                'used': memory_used,
                'percent': f"{memory_percent}%"
            },
            'gpu': gpu_info,
            'server_time': server_time
        }
    }

def get_thread_info():
    threads = []
    for thread in threading.enumerate():
        # Get thread stack trace
        frame = sys._current_frames().get(thread.ident)
        stack_trace = None
        if frame:
            stack_trace = ''.join(traceback.format_stack(frame))
        
        thread_info = {
            'id': thread.ident,
            'name': thread.name,
            'daemon': thread.daemon,
            'native_id': thread.native_id,
            'status': 'running' if thread.is_alive() else 'stopped',
            'stack_trace': stack_trace
        }
        threads.append(thread_info)
    
    # Get thread metrics
    metrics = {
        'total': threading.active_count(),
        'active': len([t for t in threading.enumerate() if t.is_alive()]),
        'daemon': len([t for t in threading.enumerate() if t.daemon]),
    }
    
    return {'threads': threads, 'metrics': metrics}

def check_ollama_status(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        latency = f"{(time.time() - start_time) * 1000:.0f}ms"
        
        if response.status_code == 200:
            return {
                'status': 'operational',
                'latency': latency,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'details': f"Available models: {len(response.json().get('models', []))}"
            }
        else:
            return {
                'status': 'incident',
                'latency': latency,
                'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'details': f"API returned status code {response.status_code}"
            }
    except requests.exceptions.ConnectionError:
        return {
            'status': 'outage',
            'latency': 'N/A',
            'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'details': 'Connection failed - Is Ollama running?'
        }
    except Exception as e:
        return {
            'status': 'incident',
            'latency': 'N/A',
            'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'details': str(e)
        }

def check_service_status(service_name, url):
    if service_name == 'Ollama':
        return check_ollama_status(url)
    
    # Default status check for other services
    return {
        'status': 'operational',
        'latency': '100ms',
        'last_checked': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'details': 'Service is running'
    }

def get_ollama_logs():
    try:
        # On macOS, Ollama logs can be accessed via system log
        cmd = "log show --predicate 'process == \"ollama\"' --style syslog --last 30m"
        output = subprocess.check_output(cmd, shell=True).decode()
        
        logs = []
        for line in output.split('\n'):
            if line.strip():
                # Parse syslog format
                try:
                    # Extract timestamp and message
                    timestamp = line[:15]  # Timestamp is usually in the first 15 characters
                    content = line[15:].strip()
                    
                    logs.append({
                        'timestamp': timestamp,
                        'content': content
                    })
                except Exception as e:
                    print(f"Error parsing log line: {e}")
                    continue
        
        return logs
    except Exception as e:
        print(f"Error getting Ollama logs: {e}")
        return []

@app.route('/')
def status_page():
    services_status = {}
    for service_name, url in SERVICES.items():
        services_status[service_name] = check_service_status(service_name, url)
    
    # Add system metrics
    services_status['System Resources'] = get_system_metrics()
    
    return render_template('status.html', services=services_status)

@app.route('/api/status')
def api_status():
    services_status = {}
    for service_name, url in SERVICES.items():
        services_status[service_name] = check_service_status(service_name, url)
    
    # Add system metrics
    services_status['System Resources'] = get_system_metrics()
    
    return jsonify(services_status)

@app.route('/logs')
def logs_page():
    return render_template('logs.html')

@app.route('/api/logs')
def api_logs():
    logs = get_ollama_logs()
    return jsonify({'logs': logs})

@app.route('/threads')
def threads_page():
    return render_template('threads.html')

@app.route('/api/threads')
def api_threads():
    return jsonify(get_thread_info())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)

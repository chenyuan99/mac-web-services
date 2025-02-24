# Mac Web Services Documentation

## Overview

Mac Web Services is a modern web application designed to monitor and manage various services and system resources on macOS. It provides real-time monitoring of system status, service health, network connections, and application threads.

## Features

### Status Page

The main dashboard that provides an overview of all monitored services and system resources.

#### Service Monitoring
- Real-time service status checks
- Response time monitoring
- Service availability tracking
- Automatic refresh capability

#### System Resources
- CPU usage and core count
- Memory utilization
- GPU information
- Server time with timezone

### Ollama Integration

Dedicated monitoring and management for Ollama services.

#### Status Monitoring
- Service health checks
- API endpoint monitoring
- Available models listing
- Response time tracking

#### Logs Viewer
- Real-time log streaming
- Auto-scroll functionality
- Timestamp filtering
- System log integration

### Thread Monitor

Comprehensive thread monitoring and management interface.

#### Features
- Real-time thread status
- Thread lifecycle tracking
- Stack trace visualization
- Thread metrics dashboard
- Auto-refresh capability

#### Metrics
- Total thread count
- Active threads
- Daemon threads
- Peak thread count

### Port Monitor

Network connection and port monitoring system.

#### Features
- TCP/UDP connection tracking
- Process-port mapping
- Connection status monitoring
- Advanced filtering system

#### Connection Details
- Protocol information
- Local/Remote addresses
- Port numbers
- Process information
- Connection states

## Technical Details

### Architecture

The application is built using:
- Flask web framework
- Python 3.10+
- psutil for system monitoring
- HTML5/CSS3 for frontend
- JavaScript for real-time updates

### API Endpoints

#### Status API
- `/` - Main status page
- `/api/status` - Service status data
- `/api/system` - System resource data

#### Logs API
- `/logs` - Logs viewer page
- `/api/logs` - Log data endpoint

#### Thread API
- `/threads` - Thread monitor page
- `/api/threads` - Thread data endpoint

#### Port API
- `/ports` - Port monitor page
- `/api/ports` - Port and connection data

## Installation

1. System Requirements:
   - Python 3.10 or higher
   - macOS operating system
   - Ollama (optional)

2. Dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Configuration:
   - Default port: 5002
   - Host: 0.0.0.0 (accessible from network)
   - Debug mode: Enabled in development

## Usage Guide

### Starting the Service

```bash
python3 src/status_page.py
```

### Accessing the Interface

1. Open your web browser
2. Navigate to `http://localhost:5002`
3. The status page will load automatically

### Monitoring Features

1. Status Page:
   - View service health
   - Monitor system resources
   - Check server time

2. Logs Page:
   - Access via "View Ollama Logs" button
   - Auto-scrolls to new logs
   - Configure refresh rate

3. Thread Monitor:
   - Access via "View Threads" button
   - Monitor thread status
   - View stack traces

4. Port Monitor:
   - Access via "View Ports" button
   - Track network connections
   - Filter and search connections

## Troubleshooting

### Common Issues

1. Port Conflicts:
   - Default port 5002 in use
   - Solution: Modify port in source code

2. Permission Issues:
   - Port monitoring requires elevated privileges
   - Solution: Run with appropriate permissions

3. Service Connection:
   - Ollama service unreachable
   - Solution: Verify Ollama is running

### Debugging

- Check application logs
- Verify service status
- Monitor system resources
- Review network connections

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

See [LICENSE](../LICENSE) for details.

## Support

For issues and feature requests, please use the GitHub issue tracker.

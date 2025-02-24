# Server Build 2023

## Requirements

Python 3.10

## Migrated MacOS

* File Server
* Caching Server
* Time Machine Server


Since Apple already make these part of new macOS, there is not much value we could add on these


## Service status

This table shows the status of each macOS Server service, and available alternatives.

Service	Status	Alternatives

Profile Manager	Available in Server 5.12.2	Learn about choosing an MDM solution

Xsan	Removed in Server 5.12	Quantum, command-line tools built into macOS

FTP	Removed in Server 5.4	SFTP/SSH

Server Docs	Removed in Server 5.4	iCloud Documents, Apache/WebDAV

DHCP	UI tools removed in Server 5.7.1	bootpd, built into macOS

DNS	Removed in Server 5.7.1	BIND, Unbound, KnotDNS

VPN	Removed in Server 5.7.1	OpenVPN, SoftEther VPN, WireGuard

Firewall	UI tools removed in Server 5.7.1	pf firewall (built into macOS)

Mail Server	Removed in Server 5.7.1	dovecot/Postfix

Courier, KerioConnect

Calendar	Removed in Server 5.7.1	CalendarServer, DavMail, Radicale, Kerio Connect

Wiki	Removed in Server 5.7.1	MediaWiki, PmWiki, XWiki, Confluence, WordPress WMX files

Websites	UI tools removed in Server 5.7.1	Apache HTTP Server (built into macOS), Nginx, Lighttpd

Contacts	Removed in Server 5.7.1	CalendarServer, DavMail, Kerio Connect

NetBoot/NetInstall	UI tools removed in Server 5.7.1	BOOTP, TFTP, HTTP, NFS (all built into macOS), NetSUS, BSDPy

Messages	Removed in Server 5.7.1	ejabberd, Openfire, Prosody

Radius	Removed in Server 5.7.1	FreeRadius

AirPort Management	Removed in Server 5.7.1	AirPort Utility

## Mac Web Services

A modern web application for monitoring and managing macOS services, with a focus on Ollama and system resources.

### Service Status Page
- Real-time monitoring of service status
- System resource metrics (CPU, Memory, GPU)
- Server time information with timezone
- Auto-refreshing status updates
- Modern, responsive UI

### Ollama Integration
- Ollama service status monitoring
- Detailed logs viewer with auto-refresh and auto-scroll
- Available models information

### System Monitoring
- CPU usage and core count
- Memory usage (total, used, percentage)
- GPU information for Mac (integrated and discrete)
- Server time with timezone information

### Thread Monitoring
- Real-time thread monitoring
- Thread status and metrics
- Stack trace visualization
- Auto-refresh capability
- Thread lifecycle tracking

### Network Port Monitoring
- Real-time port and connection monitoring
- TCP and UDP connection tracking
- Process information for each connection
- Connection status and metrics
- Advanced filtering capabilities

## Requirements

- Python 3.10+
- macOS
- Ollama (optional, for Ollama monitoring)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mac-web-services.git
cd mac-web-services
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Usage

1. Start the service:
```bash
python3 src/status_page.py
```

2. Open your web browser and navigate to:
```
http://localhost:5002
```

3. View the status page and monitor your services.
4. Click "View Ollama Logs" to access the logs page.
5. Click "View Thread Monitor" to access the thread monitor page.
6. Click "View Port Monitor" to access the port monitor page.

## Features

### Status Page
- Monitor service status
- View system resource usage
- Check server time
- Auto-refresh capability

### Logs Page
- View Ollama service logs
- Auto-scroll functionality
- Real-time log updates
- Configurable refresh rate

### Thread Monitor Page
- View all active threads
- Monitor thread states and metrics
- Inspect thread stack traces
- Track daemon vs non-daemon threads
- Real-time updates

### Port Monitor Page
- View all active network connections
- Monitor TCP and UDP ports
- Track listening and established connections
- Filter by protocol, status, or search terms
- Process and PID information
- Real-time updates

## Legacy Services

The following macOS Server services have been migrated or removed in recent versions:

* File Server
* Caching Server
* Time Machine Server

Since Apple has integrated these services into macOS, this application focuses on monitoring modern services and system resources.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See [LICENSE](LICENSE) for details.

## References

https://www.youtube.com/watch?v=CITHNloGlnU&t=268s

https://discussions.apple.com/docs/DOC-3083
About macOS Server 5.7.1 and later - Apple Support
How to Monitor Network Traffic On an OS X Mac | IT Support Blog

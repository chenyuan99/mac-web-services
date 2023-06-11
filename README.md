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



References

https://www.youtube.com/watch?v=CITHNloGlnU&t=268s

https://discussions.apple.com/docs/DOC-3083
About macOS Server 5.7.1 and later - Apple Support
How to Monitor Network Traffic On an OS X Mac | IT Support Blog

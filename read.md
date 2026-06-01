Overview

This project is a Flask-based Linux system monitoring dashboard that I built to learn Python web development and gain hands-on experience with how applications are deployed and managed on Linux servers.

My background is primarily in IT support and systems administration, so this project was an opportunity to move beyond Bash scripting and learn how a Python application is structured, deployed, and maintained in a Linux environment.

The application displays basic system health information through a web interface, including CPU utilization, memory usage, disk usage, uptime, and other system metrics.

Goals

The primary goals of this project were:

Learn Python development using Flask
Understand how web applications are hosted on Linux
Deploy and manage an application using systemd
Configure a reverse proxy using Nginx
Work with SELinux in a real deployment scenario
Gain experience troubleshooting Linux services and networking issues
Build a project that combines Linux administration and software development
Features

Current functionality includes:

User authentication
CPU utilization monitoring
Memory usage monitoring
Disk usage monitoring
System uptime information
Live system metrics displayed through a web interface
Service management through systemd
Reverse proxy configuration with Nginx

Future enhancements may include:

Historical performance graphs
Multi-server monitoring
Alerting and notifications
User activity monitoring
Additional system health checks
Technology Stack
Backend
Python
Flask
Gunicorn
Linux Services
systemd
SELinux
Nginx
Operating System
Red Hat Enterprise Linux (RHEL)
Deployment Architecture
Browser
   |
   v
Nginx (Port 80)
   |
   v
Gunicorn (127.0.0.1:8000)
   |
   v
Flask Application

Nginx acts as the public-facing web server and reverse proxy while Gunicorn serves the Flask application internally.

Lessons Learned

This project provided hands-on experience with several concepts that are common in enterprise Linux environments:

Python virtual environments
Flask application development
Git and GitHub workflows
Linux file permissions
systemd service management
Nginx configuration
Reverse proxy architecture
SELinux troubleshooting
Application deployment and maintenance

One of the biggest takeaways from this project was understanding that deploying an application involves much more than writing code. Troubleshooting permissions, services, networking, and security settings became a significant part of the learning process.

Running the Application

Start the application service:

sudo systemctl start linux-dashboard

Check service status:

sudo systemctl status linux-dashboard

Restart the service:

sudo systemctl restart linux-dashboard
Author

Built as a learning project to develop Python, Linux administration, and application deployment skills while exploring how enterprise applications are hosted and managed on Linux servers.

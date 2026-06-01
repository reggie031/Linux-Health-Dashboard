Overview

This project is a Flask-based Linux system monitoring dashboard built to learn Python web development and gain hands-on experience with how applications are deployed and managed in Linux environments.

I also wanted to use this project to build something that could realistically be used in a work environment, not just a coding exercise. That influenced how I approached deployment, system design, and monitoring.

The application provides a web-based view of Linux system health metrics and is deployed using a production-style stack on a CentOS Linux virtual machine.

Key Features
CPU utilization monitoring
Memory usage tracking
Disk usage monitoring
System uptime reporting
Active logged-in users
Web-based dashboard interface
Session-based authentication
Tech Stack

Backend

Python
Flask
psutil
Gunicorn

Infrastructure

Nginx (reverse proxy)
systemd (service management)
SELinux (security enforcement)
CentOS Linux

Tools

Git / GitHub
Visual Studio Code
Architecture
Browser
   ↓
Nginx (Port 80)
   ↓
Gunicorn (127.0.0.1:8000)
   ↓
Flask Application
   ↓
Linux System Metrics

Nginx handles incoming traffic and forwards requests to Gunicorn, which runs the Flask application. The app collects system metrics directly from the Linux host.

Real-World Use Cases

This type of dashboard is commonly used (in more advanced forms) by system administrators and DevOps teams to monitor server health and performance.

It can be applied to:

Monitoring infrastructure health in real time
Supporting incident response and troubleshooting
Providing visibility into CPU, memory, and disk usage trends
Managing internal servers or homelab environments
Serving as a foundation for enterprise monitoring tools
What I Learned

This project helped me connect software development with Linux system administration. Along the way, I worked through real deployment challenges including:

Flask routing and application structure
Python virtual environments
Gunicorn application serving
Nginx reverse proxy configuration
systemd service creation and management
SELinux policy troubleshooting
Linux permissions and networking issues
Git and GitHub workflows

A major takeaway was understanding that deploying applications involves just as much systems and infrastructure work as writing code.

Running the Project
sudo systemctl start linux-dashboard
sudo systemctl status linux-dashboard
sudo systemctl restart linux-dashboard

Logs:

journalctl -u linux-dashboard -f
Future Improvements
Historical metrics and graphing
Multi-server monitoring support
Alerting for CPU / memory thresholds
HTTPS support
Role-based authentication
Expanded system metrics (services, processes, logs)
Purpose

This project was built as a learning exercise to develop skills in Python development, Linux system administration, and application deployment. It reflects a hands-on approach to understanding how applications are run and maintained in real Linux environments.

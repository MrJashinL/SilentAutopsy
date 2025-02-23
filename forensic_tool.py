import os
import datetime
import psutil
import shutil
from jinja2 import Template
from gpt2_integration import analyze_with_gpt2

def collect_system_logs():
    logs = []
    for log_file in ['/var/log/syslog', '/var/log/auth.log']:
        if os.path.exists(log_file):
            with open(log_file, 'r') as file:
                logs.append(file.read())
    return logs

def collect_system_info():
    info = {
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_info': psutil.virtual_memory()._asdict(),
        'disk_usage': psutil.disk_usage('/')._asdict(),
        'network_connections': psutil.net_connections(),
        'running_processes': [proc.info for proc in psutil.process_iter(['pid', 'name', 'username'])]
    }
    return info

def generate_report(system_info, logs, analysis):
    template = Template("""
    <html>
    <head><title>SilentAutopsy Report</title></head>
    <body>
    <h1>SilentAutopsy Report</h1>
    <h2>Developed by Jashin L.</h2>
    <h1>System Information</h1>
    <ul>
        <li>Timestamp: {{ system_info.timestamp }}</li>
        <li>CPU Usage: {{ system_info.cpu_usage }}%</li>
        <li>Memory Info: {{ system_info.memory_info }}</li>
        <li>Disk Usage: {{ system_info.disk_usage }}</li>
        <li>Network Connections: {{ system_info.network_connections }}</li>
        <li>Running Processes: {{ system_info.running_processes }}</li>
    </ul>
    <h1>Logs</h1>
    {% for log in logs %}
        <pre>{{ log }}</pre>
    {% endfor %}
    <h1>AI Analysis</h1>
    <pre>{{ analysis }}</pre>
    </body>
    </html>
    """)
    report = template.render(system_info=system_info, logs=logs, analysis=analysis)
    report_path = '/tmp/forensic_report.html'
    with open(report_path, 'w') as file:
        file.write(report)
    return report_path

def cleanup(report_path):
    if os.path.exists(report_path):
        os.remove(report_path)

def main():
    system_info = collect_system_info()
    logs = collect_system_logs()
    logs_combined = "\n".join(logs)
    analysis = analyze_with_gpt2(logs_combined)
    report_path = generate_report(system_info, logs, analysis)
    cleanup(report_path)

if __name__ == "__main__":
    main()
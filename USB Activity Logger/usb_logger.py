import pyudev
import datetime

# Setup context and monitor
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

# Log file
log_file = "usb_log.txt"

# New callback function — accepts only 'device'
def log_event(device):
    action = device.action  # 'add' or 'remove'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    device_name = device.device_node or device.sys_name or "Unknown"
    log_entry = f"{timestamp} - USB {action.upper()} - {device_name}"
    print(log_entry)

    with open(log_file, "a") as f:
        f.write(log_entry + "\n")

# Use MonitorObserver with the corrected callback
observer = pyudev.MonitorObserver(monitor, callback=log_event, name='usb-monitor')
observer.start()

print("🔌 USB Activity Logger Running... Press Ctrl+C to stop.")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🛑 Logger stopped by user.")

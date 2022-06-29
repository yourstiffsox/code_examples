import psutil
from time import time, sleep
from emails import generate_health_email
from emails import send_email
import socket
f = True
while f == True:
    sleep(60 - time() % 60)
    cpu = psutil.cpu_percent()
    disk = psutil.disk_usage(r'c:')
    memory = psutil.virtual_memory()
    print(memory[0])
    if cpu > 80:
        message = generate_health_email('automation@example.com', 'username@example.com', 'Error - CPU usage is over 80%', 'Please check your system and resolve the issue as soon as possible.')
        send_email(message)
        f = False
    if disk[3] > 80:
        message = generate_health_email('automation@example.com', 'username@example.com', 'Error - Available disk space is lowe than 20%', 'Please check your sysytem and resolve the issue as soon as possible')
        send_email(message)
        f = False
    if memory[1] < 500000000:
        message = generate_health_email('automation@example.com', 'username@example.com', 'Error - Available memory is less than 500MB', 'Please check your system and resolve the issue as soon as possible')
        send_email(message)
        f = False
    if socket.gethostbyname('localhost') != '127.0.01':
       message = generate_health_email('automation@example.com', 'username@example.com', 'Error - localhost cannot be resolved to 127.0.0.1')
       send_email(message)
       f = False
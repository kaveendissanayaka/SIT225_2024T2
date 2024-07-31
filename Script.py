import serial
import time
import random

# Initialize the commnication
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def write_read():
    num = random.randint(1, 10)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Sending number to Arduino: {num}")
    arduino.write(bytes(str(num), 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').strip()
    if data: 
        
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Received number from Arduino: {data}")
        time_to_sleep = int(data)
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Sleeping for {time_to_sleep} seconds.")
        time.sleep(time_to_sleep)
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Woke up after sleeping.")
    
while True:
    write_read()
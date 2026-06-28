import time

while True:
    current_time = time.strftime("%I:%M:%S %p")
    print(f"🕐 {current_time}", end="\r")
    time.sleep(1)

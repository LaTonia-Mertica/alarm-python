import time
import subprocess

# this project requires a virtual environment
# to create a virtual environment: python3 -m venv alarm-clock
# to use the virtual env: source alarm/bin/activate
# to install a module: pip install modulename

alarm_time = input("Set Alarm ")
sound = "beep.mp3"
repetitions = 3

while True:
    date = time.ctime()
    current_time = date[11:16]

    if current_time == alarm_time:

        for beep in range(repetitions):
            print(beep)
            print("---")
            print("initial")
            subprocess.call(["afplay", sound])
            time.sleep(5)
            print("second")
            subprocess.call(["afplay", sound])
        break

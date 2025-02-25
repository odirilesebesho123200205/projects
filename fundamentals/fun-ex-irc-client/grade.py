import sys
import os
import subprocess
import time
import random

path_to_submission = os.path.normpath(sys.argv[1]) + "/"


def start_listener():
    # python3 irc.py listen 161.35.35.171 6667 '#programming' 'username'

    process = subprocess.Popen(
        ["python3", "irc.py",
            "listen", "161.35.35.171", "6667",
            "#testing-90210", "lmsbot"],
        cwd=path_to_submission,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(1)  # allow some time for the connection

    return process


def kill_listener(process):
    process.kill()
    process.wait()
    output = process.stdout.read().decode("utf-8")
    return output


def send_message(message):
    # python3 irc.py send 161.35.35.171 6667 '#programming' 'username'
    process = subprocess.Popen(
        ["python3", "irc.py",
            "send", "161.35.35.171", "6667",
            "#testing-90210", "lmsbot", message],
        cwd=path_to_submission,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process.wait()


listener = start_listener()
seed = random.randint(1, 1000)
message = f"Hello, world! Here's a random number: {seed}"
send_message(message)
time.sleep(1)  # time allowed to receive the message
output = kill_listener(listener)
expected_username = "<lmsbot>"

if expected_username in output and message in output:
    print("You were able to send and receive a message! Well done.")
    exit(0)
else:
    print("We weren't able to send and receive a message. Try again.")
    exit(1)

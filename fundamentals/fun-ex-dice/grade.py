import sys
import os
import subprocess

path_to_submission = os.path.normpath(sys.argv[1]) + "/"


def run_student_submission(dice, faces, rolls, weights, bins):
    process = subprocess.Popen(
        ["python3", "dice_simulator.py",
            "--dice", dice,
            "--faces", faces,
            "--rolls", rolls,
            "--weights", ",".join(map(str, weights)),
            "--bins", bins],
        cwd=path_to_submission,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process.wait()

    stdout = process.stdout.read().decode("utf-8")
    stderr = process.stderr.read().decode("utf-8")

    return stdout, stderr, process.returncode


correct = True

output, stderr, returncode = run_student_submission(
    dice="2",
    faces="6",
    rolls="1000",
    weights=[1, 2, 3, 2, 1, 5],
    bins="15"
)

if returncode != 0:
    print("Your program crashed with the following error:")
    print(stderr)
    exit(1)

if "mean" not in output.lower():
    print("I couldn't see a 'mean' in the output. Make sure you're printing the mean.")
    correct = False

if "median" not in output.lower():
    print("I couldn't see a 'median' in the output. Make sure you're printing the median.")
    correct = False

if "mode" not in output.lower():
    print("I couldn't see a 'mode' in the output. Make sure you're printing the mode.")
    correct = False

if correct:
    print("I've tested the basics and it looks like they're working. Great job!")
    exit(0)
else:
    print("Keep working!")
    exit(1)

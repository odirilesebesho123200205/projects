import sys
import os
import subprocess

path_to_submission = os.path.normpath(sys.argv[1]) + "/"


def run_student_submission(dataset):
    process = subprocess.Popen(
        ["python3", "analyze.py",
            f"datasets/{dataset}.csv", "-o", f"analysis-{dataset}/"],
        cwd=path_to_submission,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process.wait()


def grade_analysis(analysis, dataset):
    # open theirs
    try:
        with open(path_to_submission + f"analysis-{dataset}/{analysis}", "r") as file:
            theirs = file.read()
    except FileNotFoundError:
        print(f"Your {analysis} was not created.")
        return False
    # open ours
    with open(f"analysis-{dataset}/{analysis}", "r") as file:
        ours = file.read()

    if theirs != ours:
        print(
            f"{analysis} was created, but it's not quite correct. Keep thinking!")
        return False

    print(f"{analysis} was created correctly.")
    return True


datasets = [
    "simpler",
]
analyses = [
    "connections.svg",
    "piblings.svg",
    "niblings.svg",
]

correct = True

for dataset in datasets:
    run_student_submission(dataset)
    for analysis in analyses:
        if not grade_analysis(analysis, dataset):
            correct = False

if correct:
    print("All analyses were successfully created. Great job!")
    exit(0)
else:
    print("Keep working!")
    exit(1)

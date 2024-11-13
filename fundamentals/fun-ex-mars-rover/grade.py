import sys
import os
import random
import subprocess
import re

random_fun_words = [
    "nuclear_pasta",
    "quark_gluon_plasma",
    "bose_einstein_condensate",
    "entropic_gravity",
    "quantum_foam",
    "holographic_principle",
    "degenerate_matter",
    "gravitational_lens",
    "the_mitochondria_is_the_powerhouse_of_the_cell",
]

path_to_submission = os.path.normpath(sys.argv[1]) + "/"
path_to_cases = "cases/"
cases = os.listdir(path_to_cases)


def run_student_submission(instructions):
    # step 1: save the instructions as a file in the submission directory
    name = random.choice(random_fun_words) + ".txt"
    with open(path_to_submission + name, "w") as file:
        file.write(instructions)
    # step 2: run "python3 simulate_rover.py name.txt" in the submission directory
    process = subprocess.Popen(
        ["python3", "simulate_rover.py", name],
        cwd=path_to_submission,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    process.wait()
    # step 3: remove file
    os.remove(path_to_submission + name)
    # step 4: return stdout and stderr
    return normalize_output(process.stdout.read().decode()), process.stderr.read().decode()


def normalize_output(output: str):
    """
    Normalize the output to have two decimal places for all numbers.
    """
    return re.sub(r"-?\d+(\.\d+)?", lambda n: f"{float(n[0]):.2f}", output.strip())



def split_case(case):
    instructions, output = case.split("Instructions:\n")[1].split("Result:\n")
    return instructions.strip(), normalize_output(output.strip())


for case in cases:
    with open(path_to_cases + case, "r") as file:
        case_input = file.read().strip()
        instructions, output = split_case(case_input)
        stdout, stderr = run_student_submission(instructions)
        if stdout != output:
            print("I tried your program with the following instructions:")
            print(instructions)
            print("\nI expected this output:")
            print(output)
            print("\nBut your program gave me this output:")
            if stdout:
                print(stdout)
            else:
                print("(There was no output to stdout.)")
            if stderr:
                print("\nThere was also an error message:")
                print(stderr)
            exit(1)

print("All test cases passed!")
exit(0)

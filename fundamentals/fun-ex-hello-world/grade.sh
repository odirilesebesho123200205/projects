if [ ! -f $1/greet.py ]; then
    echo "File greet.py not found!"
    exit 1
fi

STUDENT_OUTPUT=$(python3 $1/greet.py)

if [ "$STUDENT_OUTPUT" == "Hello, world!\n" ]; then
    echo "Correct output!"
    exit 0
else
    echo "Incorrect output!"
    exit 2
fi
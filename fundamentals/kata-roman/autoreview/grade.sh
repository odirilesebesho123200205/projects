cp ./tests.py $1/_tests.py
cd $1

if [ -e prepare.sh ]; then
    echo "Detected prepare.sh script"
    ./prepare.sh
fi

python3 -m pytest ./_tests.py

# TODO: Put review into schema
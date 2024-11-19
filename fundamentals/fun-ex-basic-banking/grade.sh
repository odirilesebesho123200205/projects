mkdir -p $1/tests
cp tests/test_banking.py $1/tests
cd $1
python3 -m pytest -v
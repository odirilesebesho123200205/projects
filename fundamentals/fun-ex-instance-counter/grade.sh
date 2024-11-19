mkdir -p $1/tests
cp tests/test_counter.py $1/tests
cd $1
python3 -m pytest -v
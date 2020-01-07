
cd $(dirname $(pwd))

python3 setup.py build
python3 setup.py sdist

cd dist
tar -xzvf mk_pyproject-0.0.1.tar.gz
cd mk_pyproject-0.0.1
python3 setup.py install

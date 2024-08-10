pushd tools
python setup.py sdist bdist_wheel
pip install dist/test_tools-0.0.1-py3-none-any.whl --force-reinstall
popd
pf connection create -f connections/test/test_connection.yaml -n test_connection
@ECHO OFF
@REM py -m pip install --index-url https://test.pypi.org/simple/ bedbug==0.1.12
@REM pip install -i https://test.pypi.org/simple/ bedbug
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple bedbug

# 1. py-tresos

## 1.1. Introduce

The utility is the python script supporting tool for EB Tresos Studio

### 1.1.1. How to create the distribution and upload to pypi
1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

### 1.1.2. Unit test

Run `pip install pytest pytest-cov` to install pytest.

Run `pytest --cov=py_tresos --cov-report term-missing` to verify all the functionality.

### 1.1.3. How to create the document

1. Run `pip install sphinx` to install the necessary document

## 1.2. eb-plugin

To Create the java project for the EB Tresos Studio Plugin.

### 1.2.1. CLI

`eb-plugin [-c|--cfg name][-h|-help]`

```
-c|--cfg name : The TOML configure file name
-h            : Show the help information.
```

### 1.2.2. Example

**Generate the default folder for EcuInfo**

```
eb-plugin -c template.toml
```
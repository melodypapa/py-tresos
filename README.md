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

### 1.2.1. TOML configuration

| Category  | Key              | Description                                                             |
| --------- | ---------------- | ----------------------------------------------------------------------- |
| component | name             | the plugin name                                                         |
|           | author           | the author's name of the plugin                                         |
|           | company          | the company owner for the plugin                                        |
|           | version          | the version of the plugin                                               |
|           | ar_version       | the AUTOSAR version of the plugin                                       |
|           | vendor_id        | the [vender Id](https://www.autosar.org/about/vendorid/) for the plugin |
|           | ar_package       | the root package for the ARXML                                          |
|           | header_files     | the header file name list for the plugin                                |
|           | source_files     | the source file name list for the plugin                                |
|           | gen_header_files | the generated head file name list for the plugin                        |
|           | gen_source_files | the generate source file name list for the plugin                       |
|           | tresos_root      | the root path for the EB Tresos Studios                                 |
| template  | source_file      | the template name for the source file                                   |
|           | header_file      | the template name for the header file                                   |

### 1.2.2. TOML configuration example

```
[component]
name       = "Plugin_Demo"
author     = "Your Name"
company    = "Your Company"
version    = "1.0.0"
ar_version = "4.0.3"
vendor_id  = "0x0008"
ar_package = "ARRoot"

header_files = [
    "Plugin_Demo.h"
]

source_files = [
    "Plugin_Demo.c"
]

gen_header_files = [
    "Plugin_Demo_Cfg.h",
]

gen_source_files = [
    "Plugin_Demo_Cfg.c",
]

tresos_root = "X:/tresos"

[template]
source_file = ""
header_file = ""
``` 

### 1.2.3. CLI

`eb-plugin [-c|--cfg name][-h|-help]`

```
-c|--cfg name : The TOML configure file name
-h            : Show the help information.
```

### 1.2.4. Example

**Generate the default folder for Plugin Demo**

```
eb-plugin -c toml/plugin_demo.toml
```

## 1.3. eb-xpath

To Create the java project for the EB Tresos Studio XPath Plugin.

### 1.3.1. TOML configuration

| Category  | Key        | Description                          |
| --------- | ---------- | ------------------------------------ |
| component | name       | the plugin name                      |
|           | author     | the author's name of the plugin      |
|           | company    | the company owner for the plugin     |
|           | version    | the version of the plugin            |
|           | ar_version | the AUTOSAR version of the plugin    |
| java      | package    | the java package name for the plugin |
|           | class      | the java class name for the plugin   |

### 1.3.2. TOML configuration example

```
[component]
name       =   "XPath_Demo"
author     =   "Your Name"
company    =   "Your name"
version    =   "1.0.0"
ar_version =   "4.0.3"

[java]
package    =   "org.ecliipse.sdv"
class      =   "xpath_demo"
``` 

### 1.3.3. CLI

`eb-xpath [-c|--cfg name][-h|-help]`

```
-c|--cfg name : The TOML configure file name
-h            : Show the help information.
```

### 1.3.4. Example

**Generate the default folder for XPath demo**

```
eb-plugin -c toml/xpath_demo.toml
```

## 1.4. Change notes

**1.0.2**

1. The ARXML template can be customized.

**1.1.0**

1. Add the supporting to create XPath Plugin.


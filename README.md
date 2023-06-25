# C-Syntax-Validator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

A custom syntax validator for the C language, which allows you to create custom rules to validate code.
It is a useful tool to verify that the developed code is in accordance with the team's standards.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

This project use [libclang](https://github.com/llvm/llvm-project/releases/) tools to handle with C files and to create the AST. You need to install it, and set libclang installation path on PATH environment variable 


### Installing required python modules

```bash
pip install -r requirements.txt
```

## Usage

### Understanding rules files

Rules are abstractions of your team's commitments or agreements. In practice, it is a JSON file with reserved keys to indicate what do you want to check.


#### Rule format

Rule file can be understood easily splitting the file on two parts. The first one describe the [target](#acceptedtargetvalues) of this rule, what do you want to verify, to be precise what kind of token do you want to check (e.g: Variables, macros, functions, etc.).


The second part, is about the **criterion** that you want to use to validade the target token. An object is used to agrupate criterion data.

```
{
    "target":["variables","globals","macros"],
    "description": "Variable declaration name must have length lower than 31 bytes",
    "criterion":{
        "target":"length_less_than",
        "value": 31
    }

}
```


##### Criterion object

It's a simple JSON object with two reserved keys, **target** to indicate what kind of criterion is wanted to use, and **value** to indicate what is the expected value to this taget. The snippet bellow show how a criterion object is created.

```
{
    "criterion":{
        "target":"length_less_than",
        "value": 31
    }
}
```

###### Accepted Criterion target values

|   Target Value    |   Description |
|-------------------|---------------|
|"length_less_than" | Verify if target has length name lower than target informed              |
| "length_bigger_than" | Verify if target has length name bigger than target informed           |
| "prefix" |    Verify if target name has the informed prefix |
| "suffix"  |  Verify if target name has the informed suffix |
| "regex" | Verify if a node name is accept by informed regular expression|



###### Accepted target values

|   Target Value    |   Description |
|-------------------|---------------|
|  "functions"        |   This rule target are the functions declaration            |
|   "globals"        |   This rule target are the global variables                |
|   "variables"      |   This rule target are the local variables                 |
|   "macros"          |  This rule target are Macros declarations                     |

## Features



## Contributing

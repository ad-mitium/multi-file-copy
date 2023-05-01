# Multiple File Copy

A python script using `shutils` to copy a file to multiple locations.

It should be obvious, but it has to be put in writing, that you use this at your own risk.

## Usage

This script uses `shutils` to copy a file to multiple pre-specified locations.

User configurable options exist to tailor its behavior and destination locations.  All user configurable variables are located in the `config` folder.

Using the `-opt` flag will provide extended.

### **Code execution as follows:**

    python3 multi-file-copy <File> <Destination folder> 

### **Examples:**

Executing

    python3 multi-file-copy filename.ext folder_path
    python3 multi-file-copy -opt 'verbose' filename.ext folder_path

## Required to use this script *(Aside from Python 3)*

* TermColor

        pip install termcolor
* TextWrap

        pip install textwrap

## To Do

* TBD

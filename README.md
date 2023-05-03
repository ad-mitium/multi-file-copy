# Multiple File Copy

A python script using `shutil` to copy a file to multiple locations. It was getting old echoing folders through xargs (even inside a bash script) to copy a file to multiple locations when there are multiple files to copy, each going to different folder names.

It should be obvious, but it has to be put in writing, that you use this at your own risk.

## Usage

This script uses `shutil` to copy a file to multiple pre-specified locations.

User configurable options exist in `configuration.py` to tailor its behavior and default destination folder locations. All user configurable variables are located in the `config` folder.

Using the `-opt` flag will provide extended information about the copy process. `-drc` disables remote copying (for debugging purposes)

### **Code execution as follows:**

    python3 multi-file-copy <Destination folder> <File>

### **Examples:**

Executing

    python3 multi-file-copy folder_path filename.ext
    python3 multi-file-copy -opt 'verbose' folder_path filename.ext

## Required to use this script *(Aside from Python 3)*

* TermColor

        pip install termcolor
* TextWrap

        pip install textwrap

## **Precautions**

This python script **does not** have a *no-clobber* test. **Make sure the desitination is empty!**

## To Do

* Add no file clobber test (maybe)
* TBD

# Multiple File Copy

A python script using `shutil` to copy a file to multiple locations. It was getting old echoing folders through xargs (even inside a bash script) to copy a file to multiple locations when there are multiple files to copy, each going to different folder names.

It should be obvious, but it has to be put in writing, that you use this at your own risk.

## Usage

This script uses `shutil` to copy a file to multiple pre-specified locations.

User configurable options exist in `configuration.py` to tailor its behavior and default destination folder locations. All user configurable variables are located in the `config` folder.

### **Flags**

    -nc     enables overwrite protection (disabled by default)
    -drc    disables remote copying (for debugging purposes)
    -opt    when used with "verbose", it will increase the verbosity of copy output

Using the `-opt` flag will provide extended information about the copy process.

### **Code execution as follows:**

    python3 multi-file-copy <Destination folder> <File>

### **Examples:**

Executing

    python3 multi-file-copy folder_path filename.ext
    python3 multi-file-copy -nc folder_path filename.ext
    python3 multi-file-copy -opt 'verbose' folder_path filename.ext

## Required to use this script *(Aside from Python 3)*

* TermColor

        pip install termcolor
* TextWrap

        pip install textwrap

## **Precautions**

* This python script has a *no-clobber* test. You must use `-nc` or `--no-clobber` to enable this, it is not enabled by default
* ~~If you choose **not** to overwrite the file, it will exit out of the script, no skipping to the next copy location~~ Skipping the folder is now an option

## **Preserving local configuration changes**

Preserving your local configuration changes, assuming your are using git to pull the repository:

    1) Change to repository folder
    2) Enter the following commands:
       1) git stash push
       2) git checkout -- config/configurations.py
       3) git pull
       4) git stash apply 
    3) Confirm that the config/configurations.py file remains the same with your favorite editor/text viewer

## To Do

* ~~Add no file clobber test (maybe)~~
* Progress indication (still deciding how to display this)
* TBD

#!/usr/bin/env python3

action_description={
"desc" : f"""
Python script that copies a file to two or more locations using shutils.

  Usage: multi-file-copy.py [-opt='options'] <folder path> <input file>    
  Examples: python3 multi-file-copy.py create folder_path_copy_destination filename.ext  
            python3 multi-file-copy.py create -opt 'verbose' folder_path_copy_destination filename.ext

""" 
, 

"epi" : f"""    Action commands include (use -opt to specify unique options):
        verbose          Be descriptive

""" 
 }

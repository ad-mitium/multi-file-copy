#!/usr/bin/env python3

action_description={
"desc" : f"""
Python script that copies a file to two or more locations using shutils.

  Usage: multi-file-copy.py [action] [-opt='options'] <input file>    
  Examples: python3 multi-file-copy.py create filename.ext folder_path_copy_destination 
            python3 multi-file-copy.py create -opt 'verbose' filename.ext folder_path_copy_destination

""" 
, 

"epi" : f"""    Action commands include (use -opt to specify unique options):
        verbose          Be descriptive

""" 
 }

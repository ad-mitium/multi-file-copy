#!/usr/bin/env python3

import os,shutil,textwrap
from pathlib import Path


#########   Useful functions   #########
def joinpath(rootdir, targetdir):
    return os.path.join(os.sep, rootdir + os.sep, targetdir)

def exit_on_error():
    answer = input("Continue with default options? [y/N]  ").lower()
    if answer == 'y':
        print("Continuing with default options")
    else:
        print("Exiting.")
        raise SystemExit(0)
    
def check_num(num): # Sanity test for input
    limit=10        # Don't dwell on failure forever
    for i in (range(limit, -1, -1)):
        if i > 0:
            try: 
                int(num)
                # print("Valid integer: ", num)
                return num
            except ValueError:
                num=input("Please enter a valid integer: ")
                i=i-1
        else:
            raise SystemExit('Too many failures to enter a valid integer, exiting.')

def probetest(command,input_filename,test_boolean):
    composite_command = command + ' '+ '"' + input_filename + '"'
    if test_boolean:
        colors.print_blue("Probing file for information")
        os.system(composite_command)
        colors.cprint ("Command executed was:\n    ", 'green', attrs=['bold'], end=' ')
        colors.print_yellow(textwrap.fill(text=composite_command, width=defaults['display_wrap_width'], subsequent_indent='        '))
        raise SystemExit(0)

def test_path(output_folder_path, copy_status):
    if os.path.exists((output_folder_path)):
        # print(os.path.dirname(output_folder_path))
        # print(output_folder_path," exists")
        pass
    else:
        colors.print_red(textwrap.fill(text='ERROR:     "'+output_folder_path+'" does not exist', 
            width=defaults['display_wrap_width'], subsequent_indent='           '))
        if copy_status:
            colors.print_orange("Creating "+output_folder_path)
            Path(output_folder_path).mkdir( parents=True, exist_ok=True)
        else:
            colors.print_orange(textwrap.fill(text="           "+
                "If copying were enabled, '"+output_folder_path+"' would be created.", 
                width=defaults['display_wrap_width'], subsequent_indent='               '))

def copy_to_remote(location_name,full_path,output_directory,filename_ext,copy_status,opt_test):
    if opt_test == 'verbose':
        print (full_path,output_directory)
        colors.print_cyan_no_cr(location_name)
        print("", end =" ")
    if copy_status:
        test_path(full_path,copy_status)
        shutil.copy(filename_ext, full_path)
    if opt_test == 'verbose':
        colors.print_yellow_no_cr(filename_ext if len(filename_ext)<defaults['filename_wrap_width'] 
            else textwrap.fill(text=filename_ext, width=defaults['filename_wrap_width'], subsequent_indent='               '))
        print('{} copied to'.format('' if copy_status else ' would be'), end =" ")
        print('' if len(filename_ext)<defaults['filename_wrap_width'] 
            else '\n           ', end="") # new line becuase the filename was too long
        colors.print_white(textwrap.fill(text=full_path, width=defaults['foldername_wrap_width'], subsequent_indent='          ') 
            if len(filename_ext)<defaults['filename_wrap_width'] 
            else textwrap.fill(text=full_path, width=defaults['display_wrap_width'], subsequent_indent='               '))

if (__name__ == '__main__'): 
    import colors
    defaults={
        'option_wrap_width':100,
        'display_wrap_width':120,
        'filename_wrap_width':80,
        'foldername_wrap_width':80
    }

    probe='less'

    # probetest(probe,"version.py", True)
    num=check_num('8')
    print(num)
    exit_on_error()
else:
    from lib import colors
    from config.configuration import defaults

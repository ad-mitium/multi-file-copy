#!/usr/bin/env python3
# Authored by Timothy Mui 4/24/2023

import argparse
from time import strftime
from lib import version as ver
from lib import colors
from lib.action_description import action_description as act_desc
from lib.common_functions import check_num,exit_on_error,joinpath,probetest,test_path,copy_to_remote
from config.configuration import out_dir_dict


start_time= strftime('%H%M%S')
version_number = (0, 0, 0)

#out_dir_path='.'
#output_path=out_dir_path

#base_outdir='.'
#extension=''

#########   Command line interaction for user supplied variables   #########
# provide description and version info
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=act_desc['desc']
, 
epilog=act_desc['epi']
 )
#parser.add_argument('action_command', help='''Enter action option. See all actions below.''')
parser.add_argument('filename', help='''Enter input file name to copy''')
parser.add_argument('output_path', help='''Enter output directory path to copy to''')
#parser.add_argument('-c','--check-file', action='store_true',help='''Probe file for information''') 
parser.add_argument('-lc','--local-copy', action='store_false',help='''Disable copying to local folder''') 
parser.add_argument('-rc','--remote-copy', action='store_false',help='''Disable copying to remote folder''') 
parser.add_argument('-opt','--option', help='''Custom display options, options must be wrapped in apostrophes (-opt 'options') ''') 
parser.add_argument('-v','--version', action='version', version='%(prog)s {}'.format(ver.ver_info(version_number)), help='show the version number and exit')
args = parser.parse_args()

#action=args.action_command.lower()
output_filename=str(args.filename)
output_path=args.output_path

enabled_local_copy=args.local_copy
enabled_remote_copy=args.remote_copy

#TEST=args.check_file

if not (args.option == None):
    OPT_TEST=args.option.lower()
else:
    OPT_TEST=''
    
#if enabled_local_copy:
    ##output_filename_ext=joinpath(base_outdir,output_file+'.'+extension)
    #output_filename_ext=joinpath(base_outdir,output_file)
    ##colors.print_red(output_filename_ext)
#else:
    ##output_filename_ext=output_file+'.'+extension
    #output_filename_ext=output_file

colors.print_blue("Copying...")

########   Copying file to destination   ########
#colors.print_blue("Copying files to remote location.\r")
for out_dir_name, out_dir_path in out_dir_dict.items():
    #print (out_dir_name)
    #print (out_dir_path)
    full_out_path=joinpath(out_dir_path,output_path)
    test_path(full_out_path,enabled_remote_copy)
    copy_to_remote(out_dir_name,full_out_path,out_dir_path,output_filename,enabled_remote_copy,OPT_TEST)

curr_time=strftime('%H%M%S')

########   Display transcode usage time   ########
elapsed_time= int(curr_time) - int(start_time)
colors.cprint("Start time: ", 'green', attrs=['bold'], end =" ")
colors.print_yellow_no_cr(start_time)
colors.cprint("  Completed time: ", 'green', attrs=['bold'], end =" ")
colors.print_yellow_no_cr(curr_time)
colors.cprint("  Elasped time: ", 'green', attrs=['bold'], end =" ")
colors.print_yellow(elapsed_time)

colors.print_blue("\rCopying completed")

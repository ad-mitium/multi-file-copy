#!/usr/bin/env python3
# Authored by Timothy Mui 4/24/2023

import argparse
from time import strftime
from lib import version as ver
from lib import colors
from lib.action_description import action_description as act_desc
from lib.common_functions import joinpath,test_path,copy_to_remote
from config.configuration import out_dir_dict


start_time= strftime('%H%M%S')
version_number = (0, 0, 4)

#########   Command line interaction for user supplied variables   #########
# provide description and version info
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description=act_desc['desc']
, 
epilog=act_desc['epi']
 )
parser.add_argument('output_path', help='''Enter output directory path to copy to''')
parser.add_argument('filename', help='''Enter input file name to copy''')
parser.add_argument('-drc','--remote-copy-disable', action='store_false',help='''Disable copying to remote folder (for debugging)''') 
parser.add_argument('-nc','--no-clobber', action='store_true',help='''Do not overwrite existing file''') 
parser.add_argument('-opt','--option', help='''Custom display options, options must be wrapped in apostrophes (-opt 'options') ''') 
parser.add_argument('-v','--version', action='version', version='%(prog)s {}'.format(ver.ver_info(version_number)), help='show the version number and exit')
args = parser.parse_args()

output_filename=str(args.filename)
output_path=args.output_path

clobber_test=args.no_clobber
enabled_remote_copy=args.remote_copy_disable

if not (args.option == None):
    OPT_TEST=args.option.lower()
else:
    OPT_TEST=''
    
colors.print_blue("Copying...")

########   Copying file to destinations   ########
for out_dir_name, out_dir_path in out_dir_dict.items():
    copy_start_time= strftime('%H%M%S')
    if OPT_TEST == 'verbose':
        # print (out_dir_name)
        # print (out_dir_path)
        pass
    full_out_path=joinpath(out_dir_path,output_path)
    test_path(full_out_path,enabled_remote_copy)
    copy_to_remote(out_dir_name,full_out_path,out_dir_path,output_filename,enabled_remote_copy,clobber_test,OPT_TEST)
    copy_end_time= strftime('%H%M%S')
    copy_elapsed_time= int(copy_end_time) - int(copy_start_time)
    colors.cprint("  Copy time: ", 'green', attrs=['bold'], end =" ")
    colors.print_yellow(copy_elapsed_time)


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

#!/usr/bin/env python3

defaults={
    'option_wrap_width':100,
    'display_wrap_width':120,
    'filename_wrap_width':80,
    'foldername_wrap_width':80
}

# Copy pattern to add more locations
keyname1='Local Dir'    # Reference key name
out_dir1='M:'    # Location of output directory to copy output file to
keyname2='Storage  '    # Reference key name
out_dir2='N:'    # Location of output directory to copy output file to

out_dir_dict={     # If addtional output directories are needed, add here
    keyname1:out_dir1,
    keyname2:out_dir2
    }

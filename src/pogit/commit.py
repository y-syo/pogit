# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    commit.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:21:53 by adjoly            #+#    #+#              #
#    Updated: 2025/01/28 21:47:45 by mmoussou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

from pogit.help import Help
from pogit.const import C_TYPES, C_ICONS, default_commit_msg, commit_format

def commit():
    if len(sys.argv) < 3 or sys.argv[2] not in C_TYPES:
        print(Help.man(0))
        exit(0)
    c_type = sys.argv[2]
    c_denom = ""
    c_msg = ""
    c_final = ""
    files = ""
    args = sys.argv
    if "-f" in args:
        files = ' '.join(args[args.index("-f") + 1].split(','))
        args.pop(args.index("-f") + 1)
        args.pop(args.index("-f"))
    if "-d" in args:
        c_denom = f'({args[args.index("-d") + 1]})'
        args.pop(args.index("-d") + 1)
        args.pop(args.index("-d"))

    #if "--doc" in args:
    #    put a funny message about rust

    if (len(args) == 3):
        c_msg = default_commit_msg[c_type]
    else:
        c_msg = ' '.join(args[3:])
    if (c_type not in C_TYPES):
        print("Error: type is not valid.")
        exit(0)

    c_final = commit_format
    c_final = c_final.replace('%i', C_ICONS[c_type])
    c_final = c_final.replace('%t', c_type)
    c_final = c_final.replace('%d', c_denom)
    c_final = c_final.replace('%m', c_msg)
    if files:
        #print(f'git add {files}')
        os.system(f'git add {files}')
    #print(f'git commit -m "{c_final}"')
    os.system(f'git commit -m "{c_final}"')

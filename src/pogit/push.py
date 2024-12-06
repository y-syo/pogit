# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    push.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:31:18 by adjoly            #+#    #+#              #
#    Updated: 2024/12/05 17:37:10 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys

from pogit.remotes import remote_list

def push():
    if (len(sys.argv) > 3):
        print("Error: Bad usage.")
        exit(0)
    if (len(sys.argv) == 3):
        branch = sys.argv[2]
    else:
        branch = "master"
    remotes = remote_list()
    for remote in remotes:
        os.system("git push " + remote + " " + branch)

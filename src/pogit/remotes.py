# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    remotes.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:31:28 by adjoly            #+#    #+#              #
#    Updated: 2024/12/05 17:36:52 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from pogit.gitRepo import get_git_repo

def remote_list():
    file = open(get_git_repo(os.getcwd()) + "/.git/config")
    remotes=[]
    for line in file:
        if "[remote" in line:
            remotes.append(line[9:-3])
    file.close()
    return (remotes)

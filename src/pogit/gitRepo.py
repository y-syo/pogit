# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gitRepo.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:10:56 by adjoly            #+#    #+#              #
#    Updated: 2024/12/05 17:36:35 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def check_git_repo(dir):
    root_dir = os.path.splitdrive(os.path.abspath( os.getcwd() ))[0] + os.sep
    while (dir != root_dir):
        if (".git" in os.listdir(dir)):
            return True
        os.chdir('..')
        dir = os.getcwd()
    return False

def get_git_repo(dir):
    while (dir != "/"):
        if (".git" in os.listdir(dir)):
            return dir
        os.chdir('..')
        dir = os.getcwd()

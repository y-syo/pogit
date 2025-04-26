# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmoussou <mmoussou@student.42angouleme.fr  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/16 13:58:26 by mmoussou          #+#    #+#              #
#    Updated: 2025/04/26 18:03:02 by mmoussou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# ------------ modules ------------

import sys
import os

# -------- local modules ----------

from pogit.push import push
from pogit.help import Help
from pogit.commit import commit
from pogit.colors import Colors
from pogit.const import COMMANDS
from pogit.__init__ import __version__
from pogit.config import get_user_conf
from pogit.gitRepo import check_git_repo, get_git_repo

# ------------ main function ------------

def main():
    if (len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] not in COMMANDS):
        print(Help.man())
        sys.exit(0)
    arg = sys.argv[1]
    if (arg == '-v' or arg == '--version'):
        print("pogit v" + __version__)
        sys.exit(0)
    if not check_git_repo(os.getcwd()):
        print(f"{Colors.RED}are you sure you're in a git repository ?{Colors.END}")
        exit(0)
    get_user_conf()
    match (COMMANDS.index(arg) % (len(COMMANDS) / 2)):
        case 0:
            commit()
        case 1:
            push()
        case 2:
            Help.man()
        case _:
            Help.man()

if __name__ == '__main__':
    main()

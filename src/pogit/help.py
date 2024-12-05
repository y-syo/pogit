# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:06:51 by adjoly            #+#    #+#              #
#    Updated: 2024/12/05 17:07:35 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pogit.colors import Colors

class Help:
    pogit = f'''{Colors.GREEN}pogit{Colors.END}

{Colors.BLUE}USAGE:{Colors.END}
  {Colors.ITALIC}pogit [COMMAND] ...{Colors.END}

{Colors.BLUE}OPTIONS:{Colors.END}
  {Colors.GREEN}-h, --help{Colors.END}        show this help message and exit.
  {Colors.GREEN}-v, --version{Colors.END}     print version.

{Colors.BLUE}COMMANDS:{Colors.END}
  {Colors.GREEN}c/commit{Colors.END}          Commit changes to the git repo.
  {Colors.GREEN}r/remote{Colors.END}          Manage the remotes of the repository.
  {Colors.GREEN}p/push{Colors.END}            Push the current project to all of the remotes.
  {Colors.GREEN}h/help{Colors.END}            Get help on a command.
'''
    push = f'''{Colors.GREEN}pogit remote push{Colors.END}
{Colors.BLUE}USAGE:{Colors.END}
  {Colors.ITALIC}pogit remote push <branch>{Colors.END}
'''
    commit = f'''{Colors.GREEN}pogit commit{Colors.END}

{Colors.BLUE}USAGE:{Colors.END}
  {Colors.ITALIC}pogit commit <message> -f <files> -d <denominator>
  pogit c <type> <(optional)denominator> <message>{Colors.END}

{Colors.BLUE}TYPE:{Colors.END}
  what's this commit about.

    {Colors.GREEN}clean:{Colors.END}    「🗑️」 clean(_): cleaned project.
    {Colors.GREEN}feat:{Colors.END}     「✨」 feat(_): added a very cool feature !
    {Colors.GREEN}init:{Colors.END}     「🎉」 init(_): hello world !
    {Colors.GREEN}norm:{Colors.END}     「✏️」 norm(_): normed project.
    {Colors.GREEN}test:{Colors.END}     「🚧」 test(_): testing things, might broke.
    {Colors.GREEN}wip:{Colors.END}      「🏗️」 wip(_): work in progress, not done yet.
    {Colors.GREEN}fix:{Colors.END}      「🔨」 fix(_): fixed some things.
    {Colors.GREEN}doc:{Colors.END}      「📝」 doc(_): added documentation.

{Colors.BLUE}OPTIONS:{Colors.END}
  {Colors.GREEN}-f <files>{Colors.END}       which files should be inclued with the commit, by default, nothing will be staged.
  {Colors.GREEN}-d <denominator>{Colors.END} a prefix for the commit to point out what's the subject of the commit.

{Colors.BLUE}MESSAGE:{Colors.END}
  More precise description of the commit.
  If no message is given, there will be a default message.
'''


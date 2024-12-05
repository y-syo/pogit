# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pogit.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmoussou <mmoussou@student.42angouleme.fr  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/16 13:58:26 by mmoussou          #+#    #+#              #
#    Updated: 2024/12/05 13:40:03 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

# ------------ credits ------------

__author__ = "y-syo"
__maintainer__ = [
    # Creator main developer
    "y-syo"
    # Windows support && developer
    "KeyZox71"
    # Nix support
    "sh-koh"]
__version__ = "0.7"
__license__ = "WTFPL"

# ------------ modules ------------

import sys
import os
import tomllib
import platform

# -------- local modules ----------


# ------------ help messages ------------

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

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

# ------------ global variables ------------

COMMANDS = ["commit", "push", "help", "--version", "c", "p", "h", "-v"]


# ------------ default settings ------------

commit_format = "「%i」 %t%d: %m"

C_TYPES = ["clean",
           "feat",
           "init",
           "norm",
           "test",
           "wip",
           "fix",
           "doc"]

C_ICONS = {"clean": "🗑️",
           "feat": "✨",
           "init": "🎉",
           "norm": "✏️",
           "test": "🚧",
           "wip": "🏗️",
           "fix": "🔨",
           "doc": "📝"}


default_commit_msg = {"clean" : "cleaned project.",
                      "feat": "added a very cool feature !",
                      "init" : "hello world !",
                      "norm" : "normed project.",
                      "test" : "testing things, might broke.",
                      "wip" : "work in progress, not done yet.",
                      "fix" : "fixed some things.",
                      "doc" : "added documentation."}


# ------------ commands functions ------------

def commit():
    if len(sys.argv) < 3 or sys.argv[2] not in C_TYPES:
        print(Help.commit)
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


def get_git_repo(dir):
    while (dir != "/"):
        if (".git" in os.listdir(dir)):
            return dir
        os.chdir('..')
        dir = os.getcwd()

def remote_list():
    file = open(get_git_repo(os.getcwd()) + "/.git/config")
    remotes=[]
    for line in file:
        if "[remote" in line:
            remotes.append(line[9:-3])
    file.close()
    return (remotes)

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


def man():
    if (len(sys.argv) != 3 or sys.argv[2] not in COMMANDS):
        print(Help.pogit)
        exit(0)
    match (COMMANDS.index(sys.argv[2]) % (len(COMMANDS) / 2)):
        case 0:
            print(Help.commit)
        case 1:
            print(Help.push)
        case _:
            print(Help.pogit)


# ------------ config function ------------

def check_data(data):
    data_keys = list(data.keys())
    for i in range(len(data_keys)):
        for y in range(len(data_keys) - i - 1):
            if data_keys[i] == data_keys[y + i + 1]:
                print(f'{Colors.RED}duplicate key found in the config file.{Colors.END}')
                return -1
    if 'format' in data_keys:
        data_keys.remove('format')
    for key in data_keys:
        if not isinstance(data[key], dict):
            print(f'{Colors.RED}{key} is wrongly formatted and shouldn\'t be there.{Colors.END}')
            return -1
        commit_keys = list(data[key].keys())
        if 'icon' not in commit_keys or 'msg' not in commit_keys:
            print(f'{Colors.RED}{key} is missformatted : {("msg", "icon")["icon" not in commit_keys]} is missing{Colors.END}')
            return -1
    return False


def get_user_conf():
    #If on Linux try in XDG_CONFIG_HOME or in HOME/.config if don't exist just don't load the config file
    if platform.system() == 'Linux':
        try:
            conf_file = os.open(os.getenv('XDG_CONFIG_HOME') + 'pogit/pogit.toml','rb')
        except:
            try:
                conf_file = os.open(os.getenv('HOME') + '/.config/pogit/pogit.toml', 'rb')
            except:
                return
    #If on Windows try in LOCALAPPDATA or in USERPROFILE/.config if don't exist just don't load the config file
    elif platform.system() == 'Windows':
        try:
            conf_file = os.open(os.getenv('LOCALAPPDATA') + '\\pogit\\pogit.toml', 'rb')
        except:
            try:
                conf_file = os.open(os.getenv('USERPROFILE') + '\\.config\\pogit\\pogit.toml', 'rb')
            except:
                return
    #If on MacOS try in HOME/.config if don't exist just don't load the config file
    elif platform.system() == 'Darwin':
        try:
            conf_file = os.open(os.getenv('HOME') + '/.config/pogit/pogit.toml', 'rb')
        except:
            return
    conf_path = os.environ.get('XDG_CONFIG_HOME')
    if conf_path == None:
        conf_path = os.environ.get('HOME') + "/.config"
    conf_dir = os.open(conf_path, os.O_RDONLY)
    if "pogit" not in os.listdir(conf_dir):
        return
    os.close(conf_dir)
    conf_dir = os.open(conf_path + "/pogit", os.O_RDONLY)
    if "pogit" not in os.listdir(conf_dir):
        return
    os.close(conf_dir)
    conf_file = open(conf_path + '/pogit/pogit.toml', 'rb')
    if not conf_file:
        return
    try:
        data = tomllib.load(conf_file)
    except:
        print(f'{Colors.RED}can\'t parse the toml config file, user configuration will be ignored.{Colors.END}')
        return
    if check_data(data):
        print(f'{Colors.RED}found an error in the config file, user configuration will be ignored.{Colors.END}')
        return
    data_keys = list(data.keys())
    if 'format' in data_keys:
        global commit_format
        commit_format = data['format']
        data_keys.remove('format')
    if data_keys:
        global C_TYPES
        global C_ICONS
        global default_commit_msg
        for key in data_keys:
            C_TYPES.append(key)
            C_ICONS[key] = data[key]['icon']
            default_commit_msg[key] = data[key]['msg']


# ------------ main function ------------

def check_git_repo(dir):
    root_dir = os.path.splitdrive(os.path.abspath( os.getcwd() ))[0] + os.sep
    while (dir != root_dir):
        if (".git" in os.listdir(dir)):
            return True
        os.chdir('..')
        dir = os.getcwd()
    return False

def main():
    if (len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] not in COMMANDS):
        print(Help.pogit)
        sys.exit(0)
    arg = sys.argv[1]
    if (arg == '-v' or arg == '--version'):
        print("pogit v" + __version__)
        sys.exit(0)
    #if (".git" not in os.listdir(os.getcwd())):
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
            man()
        case _:
            print(Help.pogit)


if __name__ == '__main__':
    main()

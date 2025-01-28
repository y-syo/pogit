# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:03:41 by adjoly            #+#    #+#              #
#    Updated: 2025/01/28 21:27:36 by mmoussou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import platform
import os
import tomllib
from pogit.colors import Colors
from pogit.const import C_TYPES, C_ICONS, default_commit_msg, commit_format

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
            conf_file = open(os.getenv('XDG_CONFIG_HOME') + '/pogit/pogit.toml', 'rb')
        except:
            try:
                conf_file = open(os.getenv('HOME') + '/.config/pogit/pogit.toml', 'rb')
            except:
                return
    #If on Windows try in LOCALAPPDATA or in USERPROFILE/.config if don't exist just don't load the config file
    elif platform.system() == 'Windows':
        try:
            conf_file = open(os.getenv('LOCALAPPDATA') + '\\pogit\\pogit.toml', 'rb')
        except:
            try:
                conf_file = open(os.getenv('USERPROFILE') + '\\.config\\pogit\\pogit.toml', 'rb')
            except:
                return
    #If on MacOS try in HOME/.config if don't exist just don't load the config file
    elif platform.system() == 'Darwin':
        try:
            conf_file = open(os.getenv('HOME') + '/.config/pogit/pogit.toml', 'rb')
        except:
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

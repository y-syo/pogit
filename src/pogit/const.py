# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    const.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adjoly <adjoly@student.42angouleme.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/05 17:09:23 by adjoly            #+#    #+#              #
#    Updated: 2024/12/05 17:15:40 by adjoly           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

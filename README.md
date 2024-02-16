# pogit

> 🌸 a git wrapper for cute commits  
> *by [y-syo](https://y-syo.me)/[mmoussou](https://profile.intra.42.fr/users/mmoussou)*

## what is this all about ?

``pogit`` is a git wrapper that aims for prettier and more easily readable commit messages.

It also helps you working with multiples remotes at once.

## features

  - cool emojis and prefix to show what's the commit about:

    feature:  [✨] feat(\_):

    clean:    [🗑️] clean(\_):

    init:     [🎉] init(\_):

    norm:     [✏️] norm(\_):

    wip:      [🏗️] wip(\_):

    fix:      [🔨] fix(\_):

    doc:      [📝] doc(\_):    

  - a commit command, that will commit and add every files (be careful, for the moment this is a forced ``git add .``, this is not made for specific files commits)
  - you can push the repo, it will push on all the remotes availables
  - helpful help messages for the commands

upcomming features:
  - remote managing (why tho ? i don't see any addition i can give that the basic thing don't have)
  - init command to initialize a git repo
  - add support for subdirectories of the repo

## install

I'll make an installer later.

For the moment, move the ``pogit`` somewhere that is in your ``PATH``, or add the folder where ``pogit`` is located in your ``PATH``.

## license

This project is published under the Do What The F\*ck You Want Public License.
So have fun doing whatever the f\*ck you want ! :D

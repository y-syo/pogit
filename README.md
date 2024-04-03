# pogit

> 🌸 a git wrapper for cute commits  
> *by [y-syo](https://y-syo.me)/[mmoussou](https://profile.intra.42.fr/users/mmoussou)*

## what is this all about ?

``pogit`` is a git wrapper that aims for prettier and more easily readable commit messages.

it also helps you working with multiples remotes at once.

## features

  - cool emojis and prefix to show what's the commit about:

    feature:  [✨] feat(\_): added a very cool feature !

    clean:    [🗑️] clean(\_): cleaned project.

    init:     [🎉] init(\_): hello world !

    norm:     [✏️] norm(\_): normed project.

    wip:      [🏗️] wip(\_): testing things, might broke.

    fix:      [🔨] fix(\_): fixed some things.

    doc:      [📝] doc(\_): added documentation.

  - a commit command, that will commit and add every files (be careful, for the moment this is a forced ``git add .``, this is not made for specific files commits)
  - you can push the repo, it will push on all the remotes availables
  - helpful help messages for the commands

upcomming features:
  - flagging on the commit command for choosing specific files to add (will also possibly use a cli for that) and the denominator thing (so the one-argument only message will disapear)
  - remote managing
  - add support for subdirectories of the repo

## install

I'll make an installer later.

For the moment, move the ``pogit`` somewhere that is in your ``PATH``, or add the folder where ``pogit`` is located in your ``PATH``.

## license

This project is published under the Do What The F\*ck You Want Public License.
So have fun doing whatever the f\*ck you want ! :D

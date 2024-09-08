# pogit

> 🌸 a git wrapper for cute commits  
> *by [y-syo](https://y-syo.me)/[mmoussou](https://profile.intra.42.fr/users/mmoussou)*

## what is this all about ?

``pogit`` is a git wrapper that aims for prettier and more easily readable commit messages.

it also helps you working with multiples remotes at once.

## features

  - cool emojis and prefix to show what's the commit about:

    feature:  「✨」 feat(\_): added a very cool feature !

    clean:    「🗑️」 clean(\_): cleaned project.

    init:     「🎉」 init(\_): hello world !

    norm:     「✏️」 norm(\_): normed project.

    test:     「🚧」 test(\_): testing things, might broke.

    wip:      「🏗️」 wip(\_): work in progress, not done yet.

    fix:      「🔨」 fix(\_): fixed some things.

    doc:      「📝」 doc(\_): added documentation.

  - push to multiple remotes easily !

  - 

upcomming features:
  - an optional config file to change the formatting and tweak some future options like a norm check
  - a 42norm checking that puts a warning flag when you commit not-normed code
  - remote managing

## install

I'll make an installer later (maybe (probably not i'm too lazy hehe (i love parenthesis))).

For the moment, move the ``pogit`` somewhere that is in your ``PATH``, or add the folder where ``pogit`` is located in your ``PATH``.

### nix 

#### nix profile

```bash
nix profile install github:y-syo/pogit#default
```

#### system packages

flake.nix
```nix
{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release24.05";
    pogit = {
      url = "github:y-syo/pogit";
      inputs.nixpkgs.follows = "nixpkgs" # to use your nixpkgs instance instead of the provided one
    };
    ...
  };
}
```

configuration.nix
```nix
{ pkgs, inputs, ...}:
{
  environment.systemPackages = [
    inputs.pogit.packages.${pkgs.system}.default
  ];
}
```

#### with home-manager module

```nix
{ inputs, ... }:
{
  imports = [
    # Importing the module to have access to options.
    inputs.pogit.homeManagerModules.default
  ];

  programs.pogit = {
    enable = true;
    #package = inputs.pogit.packages.${pkgs.system}.pogit; # Default package can be changed here.
    config = {
      format = "TODO"; # To format the text
      custom-commit-name = {
        icon = "🐶";
        default_msg = "a default message.";
      };
    };
  };
}
```

## license

This project is published under the Do What The F\*ck You Want Public License.
So have fun doing whatever the f\*ck you want ! :D

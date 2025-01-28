# pogit

> 🌸 a git wrapper for cute commits  
> *by [y-syo](https://y-syo.me)/[mmoussou](https://profile.intra.42.fr/users/mmoussou)*

## what is this all about ?

``pogit`` is a git wrapper that aims for prettier and more easily readable commit messages.

it also helps you working with multiples remotes at once.

## documentation

check the [wiki](https://github.com/y-syo/pogit/wiki) (wip, not actually there for now but we're working on it, trust me pls)

## install

### via pip
```
pip install git+https://github.com/y-syo/pogit
```

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
    # importing the module to have access to options.
    inputs.pogit.homeManagerModules.default
  ];

  programs.pogit = {
    enable = true;
    #package = inputs.pogit.packages.${pkgs.system}.pogit; # default package can be changed here.
    config = {
      format = "TODO"; # to format the text
      custom-commit-name = {
        icon = "🐶";
        default_msg = "a default message.";
      };
    };
  };
}
```

## commit guideline

pogit has a [commit guideline](https://github.com/y-syo/pogit/wiki/Commit-guideline) that you can use for all your project :tada:

## license

This project is published under the Do What The F\*ck You Want Public License.
So have fun doing whatever the f\*ck you want ! :D

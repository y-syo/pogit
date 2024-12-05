{
  description = "🌸 a git wrapper for cute commits.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs =
    inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
      ];

      perSystem =
        { self', pkgs, ... }:
        {
          formatter = pkgs.nixfmt-rfc-style;
          devShells.default = pkgs.mkShell {
            packages = with pkgs; [
              self'.packages.pogit.nativeBuildInputs
              python312
              python312Packages.pip
              python312Packages.build
              python312Packages.wheel
              python312Packages.setuptools
            ];
          };

          packages = {
            default = self'.packages.pogit;
            pogit = pkgs.callPackage ./nix { };
          };
        };

      flake.homeManagerModules = {
        default = inputs.self.homeManagerModules.pogit;
        pogit = import ./nix/hm-module.nix inputs.self;
      };
    };
}

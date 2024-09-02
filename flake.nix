{
  description = "A development environment for this python project";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" "aarch64-linux" ];

      perSystem = { self', pkgs, ... }:
      {
        formatter = pkgs.nixfmt-rfc-style;
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [ python3 ];
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

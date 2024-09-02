self: {
  config,
  lib,
  pkgs,
  ...
}:
let
  inherit (lib.types) nullOr package;
  inherit (lib.options) mkOption mkEnableOption literalExpression;
  inherit (lib.modules) mkIf;

  cfg = config.programs.pogit;
  tomlFormat = pkgs.formats.toml { };
in
{
  options.programs.pogit = {
    enable = mkEnableOption "pogit";
    package = mkOption {
      type = package;
      default = self.packages.${pkgs.stdenv.hostPlatform.system}.pogit;
    };
    config = mkOption {
      type = nullOr tomlFormat.type;
      default = { }; 
      description = ''
        Add custom commits to extend pogit.
      '';
      example = literalExpression ''
        {
          format = "...";
          cat = {
            icon = "🐶";
            default_msg = "dog";
          };
        }
      '';
    };
  };

  config = mkIf cfg.enable {
    home.packages = [ cfg.package ];
    xdg.configFile."pogit/pogit.toml" = mkIf (cfg.config != { }) {
      source = tomlFormat.generate "pogit-config" cfg.config;
    };
  };
}

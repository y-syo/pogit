{
  python3,
  ...
}:
python3.pkgs.buildPythonApplication {
  name = "pogit";
  version = "0.5.0";
  src = ../.;
}

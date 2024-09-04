{
  python3,
  ...
}:
python3.pkgs.buildPythonApplication {
  name = "pogit";
  version = "0.6.1";
  src = ../.;
}

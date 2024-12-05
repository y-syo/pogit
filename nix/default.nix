{
  python3,
  git,
  poetry,
  ...
}:
python3.pkgs.buildPythonApplication {
  name = "pogit";
  version = "0.7";
  src = ../.;
  nativeBuildInputs = [ poetry git ];
}

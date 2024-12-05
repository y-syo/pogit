{
  python3,
  git,
  ...
}:
python3.pkgs.buildPythonApplication {
  name = "pogit";
  version = "0.7";
  src = ../.;
  nativeBuildInputs = [ git ];
}

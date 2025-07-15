{
  python3Packages,
  git,
  ...
}:
python3Packages.buildPythonApplication {
  name = "pogit";
  version = "0.7";
  src = ../.;
  pyproject = true;
  nativeBuildInputs = [
    git
  ];
  build-system = with python3Packages; [
    setuptools
  ];
}

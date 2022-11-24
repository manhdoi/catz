# catz

## Install

```commandline
python setup.py install
```

## Test

```commandline
pytest
coverage run -m pytest
coverage report
coverage html
```

## Tagging

```commandline
cat version.txt | awk '{system("git tag -a "$1" -m \"version\"")}'
```

Python command line for the [kubernetes](http://kubernetes.io/) API.

## Installation

From source:

```
git clone $PROYECT
cd k8s-command-line
```

## Examples

help:

``` shell
python3 main.py -h
```

list all pods:

``` shell
python3 main.py -ns default -a list -k pod -nm list
```

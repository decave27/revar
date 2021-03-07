# revar
![PyPI](https://img.shields.io/pypi/v/revar?logo=pypi)
![PyPI - License](https://img.shields.io/pypi/l/revar)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Various types of multi-replace

## Installation

```bash
pip install revar
```
## Examples
Input
```python
import revar
text = "Hello, $username$\nNice to meet $who$"
output = revar.replace(text, {"$username$": "decave27", "$who$": "you"})
print(output)
```
Output
```
Hello, decave27
Nice to meet you
```
```python
import revar

r = revar.Revar(prefix="$")
output = r.replace("Hello, $username\nNice to meet $who", username="decave27", who="you")
print(output)
```
Output
```
Hello, decave27
Nice to meet you
```

## Discord Server
https://discord.gg/SksjBSvuMn


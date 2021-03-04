from typing import Dict, Union

__all__ = ["replace"]
__version__ = "0.1"
__author__ = "decave27"

def replace(
    source: Union[list, set, str, tuple], var: Dict[str, Union[str, int, bool, float]]
):
    """
    Replace specific values ​​with custom variables.

    Parameters
    ==========
    source: typing.Union[list, set, str, tuple]
        string or list before being replaced.
    var: typing.Dict[str, typing.Union[str, int, bool, float]]
        This is the variable setting for conversion.
    """
    if isinstance(source, (tuple, list, set)):
        for oldstr, newstr in var.items():
            if oldstr in old:
                source = [newstr if i == oldstr else i for i in source]
    if isinstance(source, str):
        for oldstr, newstr in var.items():
            source = source.replace(oldstr, newstr)
    return source



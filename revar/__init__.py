# -*- coding: utf-8 -*-
from typing import Dict, Union

"""
Revar
~~~~~~~~~~~~~~~~~~~
Replace specific values ​​with custom variables.

:copyright: (c) 2021 decave27
:license: MIT, see LICENSE for more details.

"""
__all__ = ["replace", "Revar"]
__version__ = "0.3"
__author__ = "decave27"
__license__ = "MIT"
__copyright__ = "Copyright 2021 decave27"


def replace(
    source: Union[list, set, str, tuple], var: Dict[str, Union[str, int, bool, float]]
) -> None:
    """
    Various types of multi-replace.

    Parameters
    ==========
    source: typing.Union[list, set, str, tuple]
        string or list before being replaced.
    var: typing.Dict[str, typing.Union[str, int, bool, float]]
        This is the variable setting for conversion.
    """
    if isinstance(source, (tuple, list, set)):
        for oldstr, newstr in var.items():
            if oldstr in source:
                source = [newstr if i == oldstr else i for i in source]
    if isinstance(source, str):
        for oldstr, newstr in var.items():
            source = source.replace(oldstr, newstr)
    return source


class Revar:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix

    """
    Various types of multi-replace with prefix.

    Parameters
    ==========
    prefix : str
        Prefix to custom variable.

    """

    def replace(self, source: Union[list, set, str, tuple], **var) -> None:
        """
        Various types of multi-replace with prefix.

        Parameters
        ==========
        source: typing.Union[list, set, str, tuple]
            string or list before being replaced.
        var: typing.Dict[str, typing.Union[str, int, bool, float]]
            This is the variable setting for conversion.
        ==========

        Example

        ```py
        revar.Revar.replace(source, var1="hello", var2="world")
        ```
        """
        if isinstance(source, (tuple, list, set)):
            for oldstr, newstr in var.items():
                if not oldstr in source:
                    source = [
                        newstr if i == (self.prefix + oldstr) else i for i in source
                    ]

        if isinstance(source, str):
            for variables in var.items():
                source = source.replace(self.prefix + variables[0], variables[1])
        return source

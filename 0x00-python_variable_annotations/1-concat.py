#!/usr/bin/env python3
"""
This string concats two strings
"""


def concat(str1: str, str2: str) -> str:
    """
    Concats two strings.

    Args:
  str1 (str): First string.
  str2 (str): Second string.
  Returns:
  str: The oncatenated strings.
  """
    rslt: str = "{}{}".format(str1, str2)
    return rslt

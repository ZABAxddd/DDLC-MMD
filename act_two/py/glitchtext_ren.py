# This file contains the Python code for the glitched/corrupted text that appears in DDLC during Act 2-4 of DDLC.

# The code logic is the same as the original game, only rewritten to use the Ren'Py's `_ren.py` approach for Python
# code.

import random

"""renpy
init python:
"""


def glitchtext(length: int) -> str:
    """
    Generates a string of random unicode characters of a specified length.

    :param length: The length of the string to generate.

    :type length: int
    :return: A string of random unicode characters.
    :rtype: str
    """
    nonunicode = (
        "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞß"
        "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    )
    return "".join(random.choice(nonunicode) for _ in range(max(0, length)))

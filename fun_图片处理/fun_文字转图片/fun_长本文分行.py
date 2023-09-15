import textwrap


def fun_长本文分行(text: str, width: int) -> list[str]:
    text = textwrap.fill(text=text, width=width)
    text_list = text.split("\n")
    return text_list

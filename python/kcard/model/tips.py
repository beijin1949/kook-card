"""
小提示模块
"""
from khl.card import *


def tips_text(logo_url: str, content: str, color: str = "#409EFF") -> CardMessage:
    """
    小提示卡片，左边展示，在左边展示卡片图片
    :param logo_url: 图片URL链接
    :param content::内容
    :param color: 卡片颜色
    :return: CardMessage
    """
    c = Card(color=color)
    c.append(Module.Context(Element.Image(src=logo_url), Element.Text(content),))
    return CardMessage(c)

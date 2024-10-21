"""
品牌模块
"""
from khl.card import *


def logo_text(logo_url: str, content: str, color: str = "#409EFF") -> CardMessage:
    """
    品牌卡片，顶部展示，在顶部展示卡片图片
    :param logo_url: 图片URL链接
    :param content::内容
    :param color: 卡片颜色
    :return: CardMessage
    """
    c = Card(color=color)
    c.append(Module.Container(Element.Image(src=logo_url, size=Types.Size.SM)))
    c.append(Module.Section(content))
    return CardMessage(c)

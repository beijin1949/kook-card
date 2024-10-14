from khl.card import *


def base(text: str, color: str = "#0067C0", title: str = "", show_divider: bool = True) -> CardMessage:
    """
    生成基础卡片
    :param text: 展现的文本
    :param color: 卡片颜色，默认深蓝#0067C0
    :param title: 标题的内容，为空则不显示
    :param show_divider: 是否在有标题的情况下显示分割线
    :return:
    """
    c = Card(color=color)
    if title != "":
        c.append(Module.Header(title))
        if show_divider: c.append(Module.Divider())
    c.append(Module.Section(text))
    return CardMessage(c)

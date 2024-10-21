from khl.card import *
from kcard import base
from typing import Literal


def reply_status(text: str, status: Literal["success", "warning", "error"] = "success",
                 show_divider: bool = False) -> CardMessage:
    """
    状态消息卡片，用于状态提示，代码块版本请用 reply_status_code
    :param text: 提示的内容
    :param status: 状态值,默认success，此处应当有填对应的状态值，如果需要用到自定义的颜色，请使用base函数
    :param show_divider: 是否在有标题的情况下显示分割线
    :return: CardMessage
    """
    color_map = {"success": "#67C23A", "warning": "#E5A23C", "error": "#F46C6C"}
    title_map = {"success": "✅ 操作成功", "warning": "⚠ 注意警告", "error": "❌ 出现错误"}
    return base(text=text, color=color_map.get(status, "success"), title=title_map.get(status, "info"),
                show_divider=show_divider)


def reply_tips(text: str, color: str = "#409EFF", show_divider: bool = True) -> CardMessage:
    """
    提示框，默认是浅蓝色边框，支持自定义颜色
    :param text: 提示的内容
    :param color: 边框颜色，默认浅蓝色(#409EFF)
    :param show_divider: 状态值，此处应当有填对应的状态值，
    :return: CardMessage
    """
    return base(text=text, color=color, title="💡 Tips", show_divider=show_divider)


def reply_status_code(text: str, status: Literal["success", "warning", "error"] = "success") -> CardMessage:
    """
   使用代码块代替分割线，给出不一样的展示效果
   :param text: 提示的内容
   :param status: 状态值，默认success，此处应当有填对应的状态值，如果需要用到自定义的颜色，请使用base函数
   :return: CardMessage
   """
    color_map = {"success": "#67C23A", "warning": "#E5A23C", "error": "#F46C6C"}
    title_map = {"success": "✅ 操作成功", "warning": "⚠ 注意警告", "error": "❌ 出现错误"}
    return base(text=f"```\n{text}\n```", color=color_map.get(status, "success"), title=title_map.get(status, "info"),
                show_divider=False)

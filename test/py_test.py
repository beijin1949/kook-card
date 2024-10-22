import khl

import kcard
from a_config import bot_config

bot = khl.Bot(token=bot_config['token'])


@bot.command("test_base")
async def test_base():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.base("测试基础模板"))


@bot.command("test_status_1")
async def test_status_1():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_status(text="状态测试:成功", status="success"))


@bot.command("test_status_2")
async def test_status_2():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_status(text="状态测试：警告", status="warning"))


@bot.command("test_status_3")
async def test_status_3():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_status(text="状态测试：失败", status="error"))


@bot.command("test_tips")
async def test_tips():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_tips(text="提示"))

@bot.command("test_status_code")
async def test_status_code_1():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_status_code(text="状态测试-代码块版本:成功", status="success"))

@bot.command("logo_text")
async def logo_text():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.logo_text(logo_url="https://s21.ax1x.com/2024/10/21/pAabljS.png",content="kook card是一款非常方便的卡片模板生成工具，如果你是不想写开发者的开发者，就可以来试试！"))


@bot.command("tips_test")
async def logo_tips():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.logo_tips(logo_url="https://img.kookapp.cn/avatars/2024-10/19/cpu28439Ym06j06j.png",content="kook card是一款非常方便的卡片模板生成工具"))

@bot.command("logo_mini")
async def logo_mini():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.logo_mini(logo_url="https://s21.ax1x.com/2024/10/21/pAabljS.png", logo_text="KOOK Card",content="kook card是一款非常方便的卡片模板生成工具，如果你是不想写开发者的开发者，就可以来试试！"))

@bot.command("test_welcome")
async def logo_welcome():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.logo_welcome(logo_url="https://img.kookapp.cn/avatars/2024-10/19/cpu28439Ym06j06j.png",content="kook card是一款非常方便的卡片模板生成工具",desc1="内容1",desc2="内容2",bg_url="https://img.kookapp.cn/assets/2024-10/01/egTCeTdjae0kc05d.png"))

print("机器人正在运行")
bot.run()

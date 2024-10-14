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

@bot.command("test_status_code_1")
async def test_status_code_1():
    channel = await bot.client.fetch_public_channel(bot_config['test_channel'])
    await channel.send(kcard.reply_status_code(text="状态测试-代码块版本:成功", status="success"))


print("机器人正在运行")
bot.run()

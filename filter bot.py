import discord
from discord.ext import commands

game = discord.Game("메세지 삭제 권한을 꼭!!! 주세요!! 안그러면 욕설이 포함된 메세지가 삭제가 안됩니다")
app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name, '디스코드에 연결되었습니다!')
    await app.change_presence(status=discord.Status.idle, activity=game)
    print("준비완료")

cursing = ["필터링 할 말 ","시발","씨발"]   

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    message_content = message.content
    for i in cursing:
        bad = message_content.find(i)
        print(bad)
        if bad >= 0:
            await message.delete()
        await app.process_commands(message)




app.run('token here')
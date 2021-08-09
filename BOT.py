
print('Hello')


# 디스코드 봇
import discord, asyncio, random, openpyxl, traceback, subprocess, random, datetime, re
import os





access_token = os.environ["BOT_ TOKEN"]
token = access_token
client = discord.Client()


@client.event
async def on_ready():
    print('봇 이 작동시작')


@client.event
async def on_message(message):
    if message.content.startswith ("?"):
        await message.add_reaction("❓")


    if message.content.startswith ("-"):
        await message.add_reaction("🌈")

    if message.content.startswith('=청소'):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개를 지워버렸다 냥~")

#정보
    if message.content.startswith("=정보"):
        if message.content == "=정보":
            await message.channel.send("올바른 명령어는 '=정보 (유저멘션)'이다 냥~")
        else:
            try:
                user = message.guild.get_member(int(message.content.split('!')[1][0:18]))
                status = str(user.status)
                if status == "online":
                    status = "온라인🟢"
                elif status == "dnd":
                    status = "방해금지⛔"
                elif status == "idle":
                    status = "자리비움🌙"
                else:
                    status = "오프라인⚫️"
                if user.bot == False:
                    bot = "유저"
                else:
                    bot = "봇"
                userid = message.content[4:]
                resu = re.findall("/d+", userid)
                m = message.guild.get_member(int(resu[0]))
                acts = m.activities
                act = [i for i in acts if isinstance(i, discord.CustomActivity)]
                date = datetime.datetime.utcfromtimestamp(((int(message.content.split('!')[1][0:18]) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(title=f'{user.name}의 정보', colour=0x1DDB16)
                embed.add_field(name="이름", value=user.name, inline=False)
                embed.add_field(name="별명", value=user.display_name)
                embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
                embed.add_field(name="아이디", value=user.id)
                embed.add_field(name="상태", value=f"{status}", inline=False)
                text = str(act)
                if text:
                    embed.add_field(name="상태메세지", value=f"{text}\n(개발중)", inline=False)
                else:
                    embed.add_field(name="상태메세지", value=f"----", inline=False)
                embed.add_field(name="최상위 역할", value=user.top_role.mention, inline=False)
                embed.add_field(name="프로필 유형", value=bot)
                embed.set_thumbnail(url=user.avatar_url)
                await message.channel.send(embed=embed)
            except Exception as e:
                user = message.guild.get_member(int(message.content.split('@')[1][0:18]))
                status = str(user.status)
                if status == "online":
                    status = "온라인🟢"
                elif status == "dnd":
                    status = "방해금지⛔"
                elif status == "idle":
                    status = "자리비움🌙"
                else:
                    status = "오프라인⚫️"
                if user.bot == False:
                    bot = "유저"
                else:
                    bot = "봇"
                userid = message.content[4:]
                resu = re.findall("/d+", userid)
                m = message.guild.get_member(int(resu[0]))
                acts = m.activities
                act = [i for i in acts if isinstance(i, discord.CustomActivity)]
                date = datetime.datetime.utcfromtimestamp(((int(message.content.split('@')[1][0:18]) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(title=f'{user.name}의 정보', colour=0x1DDB16)
                embed.add_field(name="이름", value=user.name, inline=False)
                embed.add_field(name="별명", value=user.display_name)
                embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
                embed.add_field(name="아이디", value=user.id)
                embed.add_field(name="상태", value=f"{status}", inline=False)
                text = str(act)
                if text:
                    embed.add_field(name="상태메세지", value=f"{text}\n(개발중)", inline=False)
                else:
                    embed.add_field(name="상태메세지", value=f"----", inline=False)
                embed.add_field(name="최상위 역할", value=user.top_role.mention, inline=False)
                embed.add_field(name="프로필 유형", value=bot)
                embed.set_thumbnail(url=user.avatar_url)
                await message.channel.send(embed=embed)
                return

#뮤트
    if(message.content.split(" ")[0] == "=뮤트"):
            if(message.author.guild_permissions.manage_channels):
                try:
                   user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                   await message.guild.get_channel(message.channel.id).set_permissions(user, send_messages=False)
                   await message.add_reaction("✅")
                except Exception as e:
                    try:
                        user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                        await message.guild.get_channel(message.channel.id).set_permissions(user, send_messages=False)
                        await message.add_reaction("✅")
                    except Exception as e:
                        await message.channel.send("오류발생\n명령어가 잘못됬거나 봇에게 채널관리 권한이 없습니다")
                        return
            else:
                await message.channel.send(embed=discord.Embed(title="권한이 없습니다", color = 0xff0000))
                return

    if(message.content.split(" ")[0] == "=언뮤트"):
            if(message.author.guild_permissions.manage_channels):
                try:
                   user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                   await message.guild.get_channel(message.channel.id).set_permissions(user, send_messages=True)
                   await message.add_reaction("✅")
                except Exception as e:
                    try:
                        user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                        await message.guild.get_channel(message.channel.id).set_permissions(user, send_messages=True)
                        await message.add_reaction("✅")
                    except Exception as e:
                        await message.channel.send("오류발생\n명령어가 잘못됬거나 봇에게 권한이 없습니다")
                        return
            else:
                await message.channel.send(embed=discord.Embed(title="권한이 없습니다", color = 0xff0000))
                return



client.run(token)

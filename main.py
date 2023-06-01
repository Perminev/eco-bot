import discord
from discord.ext import commands
from settings import settings
import os, random



intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"You have just entered as {bot.user}")

#I helped the environment
@bot.command()
async def ihte(ctx):
    img_name = random.choice(os.listdir('batteries'))
    with open(f'batteries/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

#theorybatteriescompound
@bot.command()
async def tbc(message):
        await message.channel.send('Батарейка – это небольшое удобное хранилище электричества, которое может быть использовано для снабжения электроэнергией различных портативных приборов: игрушек, мелких бытовых и электронных приборов и т.п. Батарейки бывают нескольких видов в зависимости от их размеров, например, «мизинчиковые», «пальчиковые», «крона», «бочка», «таблетка». Так же батарейки подразделяются на различные типы в зависимости от состава: сухие, щелочные, литиевые. Несмотря на большое разнообразие видов батареек, принцип их работы одинаков, и связан с течением тока между различными химическими элементами, помещенными в электролит.')

@bot.command()
async def guide(message):
        await message.channel.send(' **Список комманд:**')
        await message.channel.send('> `$guide - показывает этот список`')
        await message.channel.send('> `$ihte - если ты уже помог экологии пиши эту комманду`')
        await message.channel.send('> `$tbc - теория, обобщённый рассказ о батарейке.`')
        await message.channel.send('> `$tbh - история батарейки.`')
        await message.channel.send('> `$tbn - рассказ о негативном влиянии батареек на экологию.`')
        await message.channel.send('> `$twntd - что надо делать что бы уменьшить вред экологии и окружающей среде.`')

#theorybatterieshistory
@bot.command()
async def tbh(message):
        await message.channel.send('Родоначальником батарейки считается итальянский ученый Алессандро Вольта. В 1800 году он построил первый электрохимический источник тока «вольтов столб». Он представлял собой набор кружков из меди и цинка сложенных одна на другую, а между ними были проложены прокладки из ткани, намоченной соляным раствором. Когда крайние пластины соединяли медной проволокой, по ней протекал постоянный электрический ток. Данный принцип работы, используется в батарейках в настоящее время.')

#theorybatteriesnegative
@bot.command()
async def tbn(message):
        await message.channel.send('Батарейка, выброшенная в мусорное ведро, попадает в итоге на свалку, где под воздействием воздуха, воды, снега, тепла, корпус батарейки начинает ржаветь и разрушаться. В результате, содержащиеся в ней тяжелые металлы попадают в почву, а из нее в грунтовые воды. Такие грунтовые воды являются источником питьевой воды. Учеными доказано, что вредные вещества от одной выброшенной на свалку батарейки способны отравить 20 квадратных метров почвы и до 400 литров воды.')

#theorywhatneedtodo
@bot.command()
async def twntd(message):
        await message.channel.send('Надо выкидывать использованные батарейки в специальный контейнер!')


bot.run(settings["TOKEN"])
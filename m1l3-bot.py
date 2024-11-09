import discord
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands
from bot_mantik import gen_pass

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptık')

@bot.command() # botun bir komutu tanıması için bu dekoratörü kullanırız.
async def hello(ctx): # hello adında bir komut tanımladık. ctx(context), komutun çağrıldığı yer hakkındaki bilgileri içerir.
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
#Bu komutun çalışması için, kullanıcı sohbette $hello yazmalıdır. 

@bot.command() # botun bir komutu tanıması için bu dekoratörü kullanırız.
async def pasw(ctx): # pasw adında bir komut tanımladık. ctx(context), komutun çağrıldığı yer hakkındaki bilgileri içer
    await ctx.send(gen_pass(10))
#Bu komutun çalışması için kullanıcı $pasw yazmalıdır.

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
 


bot.run("token")

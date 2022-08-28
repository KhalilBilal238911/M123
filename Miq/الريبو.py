import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
from Miq.helpers.decorators import authorized_users_only

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}"))
@authorized_users_only

async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعاده تشغيل حساب الخال**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["اوامر","اوامر الاغاني"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 هلا حبيبي اسوة راسك ؟. تفضل أمر خدمة ؟  {m.from_user.mention}!

هذني الاوامر الي تكدر تستخدمها  😃
——————×—————

⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}تشغيل  + اسم الاغنية + او الرابط من يوتيوب` ]
⧉ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشغيل_فيديو  + اسم الاغنية + او الرابط من اليوتيوب` ]
———————×———————

⧉ | لأيقاف الصوت او الفيديو مؤقتآ  ⇦ [ `{HNDLR}استئناف` ] 
⧉ | لأعاده تشغيل الصوت ⇦  [ `{HNDLR}ايقاف_الاستئناف` ]
⧉ | لأيقاف الصوت  ⇦ [ `{HNDLR}ايقاف` ] 
———————×———————

⧉ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تحميل + اسم الاغنية او الرابط` ]
⧉ | لتحميل فيديو  ⇦  [ `{HNDLR}تحميل_فيديو + اسم الاغنية او الرابط` ]
———————×———————

⧉ | لأعاده تشغيل النظام  ⇦  [ `{HNDLR}ريستارت` ]
———————×———————
 مطور نظام : @Ti_iT01
كروبنا على التليكرام :  @XX_SG"""
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 هلا حبيبي اسوة راسك ؟. تفضل أمر خدمة ؟ {m.from_user.mention}!
- للمطور : @Ti_iT01
 @XX_SG
"""
    await m.reply(REPO, disable_web_page_preview=True)

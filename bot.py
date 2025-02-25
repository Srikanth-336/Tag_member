#Copyright @ItsAttitudeking
#sys
import os, logging, asyncio

#telethon bhaiya
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

#worker
moment_worker = []

#cancel
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global moment_worker
  moment_worker.remove(event.chat_id)

#start
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Hey [🤗](https://telegra.ph/file/20d1d874ca88c223e9eb0.jpg)\nWelcome🔥🥂\n━━━━━━━━━━━━━━━━━━━━\n┏━━━━━━━━━━━━━━━━━┓\n┣★I m Highly advanced Tag Member Bot.\n┣★I can tag  members in group as well as in Channel.\n┣★Need Help hit ☛ [★Sriki★](Https://t.me/Srikanth_36)\n┗━━━━━━━━━━━━━━━━━┛\n━━━━━━━━━━━━━━━━━━━━",
                   buttons=(
                      [Button.url('🔥ᴀᴅᴅ ᴛᴀɢ ᴍᴇᴍʙᴇʀ ᴛᴏ ɢʀᴏᴜᴩ🔥', 'http://t.me/Srikibots_Mention_Bot?startgroup=true')],
                      [Button.url('⚜ᴏᴡɴᴇʀ⚜', 'Https://t.me/Srikanth_36')],
                      [Button.url('🛎ꜱᴜᴩᴩᴏʀᴛ', 'https://t.me/Sriki_Support_chat'),
                      Button.url('ᴜᴩᴅᴀᴛᴇ🔊', 'https://t.me/Attitude_Network')],
                     [Button.url('⚒ʀᴇᴩᴏ⚒', 'https://github.com/Srikanth-336/Tag_member')]
                     ),
                    link_preview=False
                   )

#help
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**[🔥](https://telegra.ph/file/20d1d874ca88c223e9eb0.jpg), ᴛᴀɢ ᴍᴇᴍʙᴇʀ ʙᴏᴛ'ꜱ ʜᴇʟᴩ ᴍᴇɴᴜ👑**\n\nCommand: /tag \n You can use this command with text you want to tell others. \n`Example: /tag Good morning!` \nYou can use this command as an answer. any message Bot will tag users to replied message"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('⚜ᴏᴡɴᴇʀ⚜', 'https://t.me/Srikanth_36'),
                      Button.url('🛎ꜱᴜᴩᴩᴏʀᴛ', 'https://t.me/Sriki_Support_chat')]
                      [Button.url('⚒ʀᴇᴩᴏ⚒', 'https://github.com/Srikanth-336/Tag_member')]
                     ),
                    link_preview=False
                   )

#Wah bhaiya full ignorebazi

#bsdk credit de dena verna maa chod dege

#tag
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.reply("Use This In Channel or Group!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply("Only Admin can use it [😌](https://telegra.ph/file/20d1d874ca88c223e9eb0.jpg).")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.reply("I can't Mention Members for Old Post!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.reply("Give me can an Argument. Ex: `/tag Hey, Where are you`")
  else:
    return await event.reply("Reply to Message or Give Some Text To Mention!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Ok tagger stopped [🔇](https://telegra.ph/file/20d1d874ca88c223e9eb0.jpg)")
        return
      if usrnum == 10:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.reply("Ok tagger stopped [🔇](https://telegra.ph/file/20d1d874ca88c223e9eb0.jpg)")
        return
      if usrnum == 10:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""



print("~~~~Started~~~~~")
print("🔥🥂Need Help Dm @Srikanth_36")
client.run_until_disconnected()

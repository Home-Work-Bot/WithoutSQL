from aiogram.types import Message
from aiogram.methods.pin_chat_message import PinChatMessage

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

prevs = dict()
curr = dict()



def createLink(msg: Message, name:str)->str:
    lnk = ""
    if msg == None:
        lnk = name
    else:
        lnk = f"<a href = 'https://t.me/{msg.chat.username}/{msg.message_id}'>{name}</a> "
    return lnk

def createMatirial(name:str, data:Message, prev:Message)->str:
    res = ""
    res += "#" + name + "\n"
    res += createLink(prev, "previous")
    if data == None:
        return (res, None)
    else:
        return (res, data)


import db
from main import bot
async def createPin(userId: int):
    #res = "<b>Hometasks</b>&&"
    chatId = db.currentUserChatId(userId)
    # print(db.currentUserChatId(userId))
    subj = db.getSubjects(chatId)
    for s in subj:
        res += createLink(None, s) + "&"
    res = res.replace("&", "\n")
    pin = await bot.send_message(text=res, chat_id=chatId,
                                  parse_mode="HTML")
    db.updatePin(chatId, pin.message_id, res)
    for s in subj:
        db.updateLast(chatId, s, pin.message_id)
    #print(db.CHATS)
    # #await PinChatMessage(chat_id=msg.chat.id, message_id=pin.message_id,
    # #                     disable_notification=True)
    
    # for s in subj:
    #     res, tmp = createMatirial(s, None, prevs[s])
    #     ans = await msg.answer(res, parse_mode="HTML")
    #     curr[s] = ans
    
    # res = "<b>Hometasks</b>&&"
    # for s in subj:
    #     res += createLink(curr[s], s) + "&"
    # res = res.replace("&", "\n")
    # pin = await bot.edit_message_text(res, pin.chat.id, pin.message_id, parse_mode="HTML")

def genChoose()->str:
    res = "Выбери предмет\n"
    subj = getData.getSubjects()
    for s in subj:
        res += "/" + s + '\n'
    return res

async def addMaterials():
    pass
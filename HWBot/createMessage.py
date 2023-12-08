from aiogram.types import Message
from aiogram.methods.pin_chat_message import PinChatMessage

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


import db
from main import bot
async def createPin(userId: int):
    chatId = db.currentUserChatId(userId)
    res = db.ParsePinned(chatId)

    pin = await bot.send_message(text=res, chat_id=chatId,
                                  parse_mode="HTML")
    
    db.updatePinId(chatId, pin.message_id)
    subj = db.getSubjects(chatId)
    for s in subj:
        db.updatePin(chatId, s, pin.message_id)
    

async def addMaterials(chatId:int, subj:str, date, data:Message):
    res = ""
    res += "#" + subj + '\n'
    res += "from " + str(date.day) + "." + str(date.month) + '\n'
    last = await bot.send_message(text=res, chat_id=chatId,
                                  parse_mode="HTML")
    db.updatePin(chatId, subj, last.message_id)
    await editPin(chatId)
    #print("FORWARD")
    await bot.forward_message(chatId, data.from_user.id, data.message_id)

async def editPin(chatId: int):
    await bot.edit_message_text(chat_id=chatId, text=db.ParsePinned(chatId), message_id=db.getPinId(chatId))
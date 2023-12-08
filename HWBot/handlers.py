from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("LOG help")

#messageLinkExample
#https://t.me/c/1401136600/18634
# @router.message()
# async def message_handler(msg: Message):
#     await msg.answer(f"message <a href = 'https://t.me/{msg.chat.username}/{msg.message_id}'> link </a> ",
#                      parse_mode="HTML")
#######################
#temporary Commands


@router.message(Command("addInstitution"))
async def start_handler(msg: Message):
    await msg.answer("LOG addInstitution")



from main import bot
from createMessage import createPin
from db import *

@router.message(Command("register"))
async def register_handler(msg: Message):
    if(userExist(msg.from_user.id)):
        await msg.answer("Вы зарегистрированы")
    else:
        await msg.answer("Процесс регистрации")

@router.message(Command("newPin"))
async def newPin_handler(msg: Message):
    await createPin(msg.from_user.id)
    
@router.message(Command("addMaterials"))
async def start_handler(msg: Message):
    await msg.answer("LOG addMaterials")
# @router.message(Command("addMatirials"))
# async def addMaterials_handler(msg: Message):
#     await msg.answer("addmatirials LOG")
#     res = genChoose()
#     await msg.answer(res)

#     await addMaterials()
#     #await msg.answer("LOG2 register")

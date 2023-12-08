from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import aiogram.methods.get_chat
import db


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Бот для модерирования домашнего задания")

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("LOG help")


@router.message(Command("addInstitution"))
async def start_handler(msg: Message):
    await msg.answer("LOG addInstitution")


@router.message(Command("register"))
async def register_handler(msg: Message):
    if(db.userExist(msg.from_user.id)):
        await msg.answer("Вы зарегистрированы")
    else:
        await msg.answer("Процесс регистрации")


from createMessage import createPin
@router.message(Command("newPin"))
async def newPin_handler(msg: Message):
    await createPin(msg.from_user.id)


from createMessage import addMaterials
@router.message(Command("addMaterials"))
async def addMaterials_handler(msg: Message):
    await addMaterials(db.currentUserChatId(msg.from_user.id), "linearAlgebra", msg.date, msg)

@router.message(Command("test"))
async def start_handler(msg: Message):
    pass
    #bot.forward_message()

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import aiogram.methods.get_chat
import db

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

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
    res = "Выберите предмет:\n"
    for s in db.getSubjects(db.currentUserChatId(msg.from_user.id)):
        res += '/' + s + '\n'
    await msg.answer(res)
    #await addMaterials(db.currentUserChatId(msg.from_user.id), "linearAlgebra", msg.date, msg)
@router.message(Command("test"))
async def start_handler(msg: Message):
    pass
    #bot.forward_message()


# SUBJECT = ""
# STATE = False
from createMessage import addMaterials
@router.message(F.text.regexp(r"/.*").group(0).as_("text"))
async def addSubject_handler(msg: Message, text:str, state: FSMContext):
    await state.set_state(Form.waitDocument)
    Form.SUBJECT = text.replace("@h0me_w0rk_bot", "")[1:]
    #SUBJECT = 
    print(Form.SUBJECT)
    #await addMaterials(db.currentUserChatId(msg.from_user.id), "linearAlgebra", msg.date, msg)

class Form(StatesGroup):
    waitDocument = State()
    SUBJECT = ""

@router.message(Form.waitDocument)
async def getFile_handler(msg: Message):
    #await msg.answer("Catch")
    print("HHHHHHHHHHHHHHHHHHHHHHHHHH")
    print(Form.SUBJECT)
    print("HHHHHHHHHHHHHHHHHHHHHHHHHH")
    await addMaterials(db.currentUserChatId(msg.from_user.id), Form.SUBJECT, msg.date, msg)

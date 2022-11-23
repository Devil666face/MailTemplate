import os
import config
from markup import Keyboard
from utils import Utils
from aiogram import Bot,Dispatcher,types,executor
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sched import scheduler


class BotState(StatesGroup):
    get_date = State()


class Bot:
    bot = Bot(token=config.TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot,storage=MemoryStorage())
    kb = Keyboard()
    utils = Utils()
    scheduler = AsyncIOScheduler()


    def __init__(self) -> None:
        Bot.scheduler.add_job(Bot.send_document,"interval",hours=24,start_date=f'2010-10-10 {config.TIME}',args=[config.ID,Bot.get_current_date()])
        Bot.scheduler.start()
        executor.start_polling(Bot.dp, skip_updates=True)


    def get_current_date() -> str:
        return datetime.now().strftime("%Y-%m-%d")


    async def send_document(id, date):
        if id!=config.ID:
            return
        doc_name = Bot.utils.get_doc_name(date)
        await Bot.bot.send_document(id, InputFile(doc_name, filename=doc_name),reply_markup=Bot.kb.keyboard())
        os.remove(doc_name)


    @dp.message_handler(commands = ['start'],state=None)
    async def start(message: types.Message):
        await message.answer('Бот запущен.',reply_markup=Bot.kb.keyboard())


    @dp.message_handler(Text(equals=kb.button(0)))
    async def print_current_date(message: types.Message, state: FSMContext):
        await Bot.send_document(message.from_user.id, Bot.get_current_date())
        

    @dp.message_handler(Text(equals=kb.button(1)))
    async def get_date_for_print(message: types.Message, state: FSMContext):
        await message.answer('Отправьте мне дату в формате: 2022-12-31',reply_markup=Bot.kb.keyboard())
        await BotState.get_date.set()
        

    @dp.message_handler(state=BotState.get_date)
    async def print_for_getting_date(message: types.Message,state: FSMContext):
        await state.finish()
        await Bot.send_document(message.from_user.id, message.text)
        

if __name__=='__main__':
    bot = Bot()
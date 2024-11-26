from aiogram import Bot,Dispatcher,types,executor
import requests
from keyboards import flags

token = "7406212123:AAFFjH_bElsd9KXO_GAn3hMR9HT2HkhNLTw"

bot = Bot(token=token)

dp = Dispatcher(bot)



flags = requests.get('http://127.0.0.1:8000/api/').json()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    print(flags)
    await message.answer("Привет! Это простой бот", reply_markup=flags)

@dp.message_handler()
async def echo(message: types.Message):
    davlat = message.text
    bayroq_url = ""
    for flag in flags:
        if davlat == flag["flag_name"]:
            bayroq_url = flag["images"]
            bayroq_url = bayroq_url[21:]
            print(bayroq_url)

    try:
        bayroq = types.InputFile(f"..{bayroq_url}")
        await message.answer_photo(photo=bayroq,caption=davlat)

    except Exception as e:
        await message.answer(f" Rasm yubormadi{davlat}.")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Чтобы получить помощь, используйте /start")




if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
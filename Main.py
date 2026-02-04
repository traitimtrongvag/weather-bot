import aiohttp
import os
import sys
import time
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not API_KEY or not BOT_TOKEN:
    raise ValueError("Thiếu API Key hoặc Bot Token!")

user_default_city = {}

def translate_weather(desc):
    translations = {
        "clear sky": "Trời quang",
        "few clouds": "Ít mây",
        "scattered clouds": "Mây rải rác",
        "broken clouds": "Mây nhiều",
        "shower rain": "Mưa rào",
        "rain": "Mưa",
        "thunderstorm": "Dông",
        "snow": "Tuyết rơi",
        "mist": "Sương mù",
        "overcast clouds": "Mây u ám",
    }
    return translations.get(desc.lower(), desc)

async def get_weather(city: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    temp = data["main"]["temp"]
                    weather_desc = data["weather"][0]["description"]
                    weather_desc_vi = translate_weather(weather_desc)
                    return f"Thời tiết ở {city}: {temp}°C, {weather_desc_vi}"
                else:
                    return "Không tìm thấy thông tin thời tiết!"
    except Exception as e:
        return f"Lỗi: {e}"

async def get_forecast(city: str) -> str:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    forecast_list = data.get("list", [])
                    if not forecast_list:
                        return "Không có thông tin dự báo thời tiết."

                    forecast_message = f"Dự báo thời tiết 5 ngày cho {city}:\n"
                    daily_forecasts = {}
                    for forecast in forecast_list:
                        dt = forecast.get("dt_txt", "").split(" ")[0]
                        if dt not in daily_forecasts:
                            daily_forecasts[dt] = forecast

                    for date, forecast in sorted(daily_forecasts.items())[:5]:
                        temp = forecast["main"]["temp"]
                        desc = forecast["weather"][0]["description"]
                        desc_vi = translate_weather(desc)
                        forecast_message += f"{date}: {temp}°C, {desc_vi}\n"
                    
                    return forecast_message
                else:
                    return "Không tìm thấy thông tin dự báo!"
    except Exception as e:
        return f"Lỗi: {e}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.message.from_user.first_name
    message = (
        f"Chào {user_name}!\n"
        "/weather <tên thành phố> - Xem thời tiết hiện tại\n"
        "/forecast <tên thành phố> - Xem dự báo thời tiết\n"
        "/setcity <tên thành phố> - Đặt thành phố mặc định\n"
        "/help - Hiển thị danh sách lệnh"
    )
    await update.message.reply_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "/weather <tên thành phố> - Xem thời tiết hiện tại\n"
        "/forecast <tên thành phố> - Xem dự báo thời tiết\n"
        "/setcity <tên thành phố> - Đặt thành phố mặc định\n"
        "/help - Hiển thị danh sách lệnh"
    )
    await update.message.reply_text(message)

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    city = " ".join(context.args) if context.args else user_default_city.get(chat_id)
    
    if not city:
        await update.message.reply_text("Vui lòng nhập tên thành phố hoặc đặt thành phố mặc định bằng /setcity.")
        return
    
    weather_info = await get_weather(city)
    await update.message.reply_text(weather_info)

async def forecast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    city = " ".join(context.args) if context.args else user_default_city.get(chat_id)
    
    if not city:
        await update.message.reply_text("Vui lòng nhập tên thành phố hoặc đặt thành phố mặc định bằng /setcity.")
        return

    forecast_info = await get_forecast(city)
    await update.message.reply_text(forecast_info)

async def setcity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    if context.args:
        city = " ".join(context.args)
        user_default_city[chat_id] = city
        await update.message.reply_text(f"Thành phố mặc định của bạn đã được đặt là: {city}")
    else:
        await update.message.reply_text("Vui lòng nhập tên thành phố sau lệnh /setcity. Ví dụ: /setcity Hanoi")

loading_done = False

def rotate_text(text, delay=0.2):
    rotations = ["|", "/", "-", "\\"]
    while not loading_done:
        for rot in rotations:
            if loading_done:
                break
            os.system('cls' if os.name == 'nt' else 'clear')     
            print(f"\r{rot} {text}", end="", flush=True)
            time.sleep(delay)
    print("\rBot is running!\n")

def main():
    global loading_done
    
    loading_thread = threading.Thread(target=rotate_text, args=("Starting bot...", 0.2))
    loading_thread.start()
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("forecast", forecast))
    app.add_handler(CommandHandler("setcity", setcity))
    
    loading_done = True
    loading_thread.join()

    app.run_polling()

if __name__ == "__main__":
    main()
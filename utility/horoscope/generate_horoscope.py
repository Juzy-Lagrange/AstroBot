import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv
import datetime
import asyncio



template = """ **Daily Horoscope:** [date]
For @[name], [zodiak sign]
**Total Score**
[total score]/10

**Money** [money score]/5
**Health** [health score]/5
**Love** [love score]/5

**Personal Horoscope:**
[horoscope]

**Advice of the day**
[advice]
"""

load_dotenv()
GEMINI_TOKEN = getenv("GEMINI_TOKEN")


genai.configure(api_key=GEMINI_TOKEN)
model = genai.GenerativeModel('gemini-pro')





async def generate_horoscope(date, username, zodiak_sign, lang):
    if lang == 'ru':
        lang = "Russian"
    elif lang == 'es':
        lang = "Spanish"
    else:
        lang = "English"

    header = "[Total score and three indicators: money, health, love]"
    body = "[general information]"
    footer = "[tip of the day]"
    general_prompt = f"Write me personal horoscope on date: {date}. Use the following structure: header: {header}, body: {body}, footer: {footer}\n"
    lang_prompt = f"Use {lang} language.\n"
    user_info_prompt = f"username: {username}, zodiak sign: {zodiak_sign}"
    body_promt = f"dont forget about emojies and user info {user_info_prompt}\n"
    format = "Don't use formatting symbols only emojies\n"
    
    result_prompt = general_prompt + lang_prompt + body_promt + format
    
    response = await model.generate_content_async(result_prompt)
    return response.text

async def generate_monthly_horoscope(date, lang):
    if lang == 'ru':
        lang = "Russian"
    elif lang == 'es':
        lang = "Spanish"
    else:
        lang = "English"
    response = await model.generate_content_async(f"Generate Horoscope on date: {date} for all zodiak signs. Use {lang} language and Don't use formatting symbols only emojies")
    return response.text
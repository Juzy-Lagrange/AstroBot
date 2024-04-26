from Bot.bot import *
from utility import GetLocalizationIfUserSession
from telegram_objects.keyboards import getAdminPanel, getAnswerAdminPanel, add_admin_panel, getMenuButtons, getProductGift
from Reports.report import *
import datetime

async def send_admin_panel(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    if user_id in admin_ids:
        await bot.delete_state(message.from_user.id, message.chat.id)
        reply_admin_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
        reply_admin_menu_markup.add(*getAdminPanel(lc))
        await bot.send_message(user_id, "Admin Panel", reply_markup=reply_admin_menu_markup)
    else:
        await bot.send_message(user_id, "GOOD LUCK, XD, Try hack this --->>> https://www.youtube.com/watch?v=dQw4w9WgXcQ")


async def post_message(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    if user_id in admin_ids:
        await bot.set_state(message.from_user.id, MyStates.wait_for_message, message.chat.id)
        await bot.send_message(user_id, "Требуется прислать/Переслать мне сообщение")
    else:
        await bot.send_message(user_id, "GOOD LUCK, XD, Try hack this --->>> https://www.youtube.com/watch?v=dQw4w9WgXcQ")


async def get_entities(message):
    start, end = 0,0
    entities = message.entities or message.caption_entities
    result_text = message
    if message.content_type in ['document', 'video', 'audio', 'voice', 'sticker', 'photo']:
        result_text = message.caption
    else:
        result_text = message.text
    res = ""
    if entities:
        for entity in entities:
            if entity.type == 'text_link':
                start = entity.offset
                end = start + entity.length
                result_text = result_text.replace(result_text[start:end] ,f'<a href="{entity.url}">{result_text[start:end]}</a>',1)

            elif entity.type == 'bold':
                start = entity.offset
                end = start + entity.length
                result_text = result_text.replace(result_text[start:end], f'<b>{result_text[start:end]}</b>',1)
              

            elif entity.type == 'blockquote':
                start = entity.offset
                end = start + entity.length
                result_text = result_text.replace(result_text[start:end], f'<blockquote>{result_text[start:end]}</blockquote>',1)
               
            elif entity.type == 'italic':
                start = entity.offset
                end = start + entity.length
                result_text = result_text.replace(result_text[start:end], f'<i>{result_text[start:end]}</i>',1)
             
            else:
                continue
    print(result_text)
    return result_text


async def get_post_message(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)

    await bot.set_state(message.from_user.id, MyStates.post, message.chat.id)
    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["post_message"] = await get_entities(message)
        data['msg'] = message

    reply_admin_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
    reply_admin_menu_markup.add(*getAnswerAdminPanel(lc))
    await bot.send_message(user_id, f"Ваше сообщение, переслать его?\n") 

    


    if message.content_type == 'text':
         await bot.send_message(user_id, data["post_message"],  parse_mode = "HTML", reply_markup = reply_admin_menu_markup)

    elif message.content_type == 'photo':
        photo = message.photo[-1].file_id  # Берем последнее фото (с наибольшим разрешением)
        caption = message.caption
        caption_entities=message.caption_entities 
        await bot.send_photo(user_id, photo, caption=data["post_message"], parse_mode = "HTML", caption_entities = caption_entities,reply_markup = reply_admin_menu_markup)




async def send_post_message(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    lc = GetLocalizationIfUserSession(user_id, message)
    selecect_subscribe_users = (telegram_user
                                    .select(telegram_user.chat_id)
                                    .where(telegram_user.subscribe_status == 1).dicts().execute())

    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        new_message = data["post_message"]
        message =  data['msg'] 

        for user in selecect_subscribe_users:
            try:
                if message.content_type == 'text':
                    await bot.send_message(user["chat_id"],  new_message, parse_mode = "HTML")
                elif message.content_type == 'photo':
                    photo = message.photo[-1].file_id  # Берем последнее фото (с наибольшим разрешением)
                    caption = new_message
                    await bot.send_photo(user["chat_id"], photo, parse_mode = "HTML", caption=caption)
            except Exception as e:
                print(e)

    await bot.delete_state(message.from_user.id, message.chat.id)
    reply_admin_menu_markup = ReplyKeyboardMarkup(resize_keyboard = True)
    reply_admin_menu_markup.add(*getAdminPanel(lc))
    await bot.send_message(user_id, f"Сообщения отправлено {len(selecect_subscribe_users)} пользователям", reply_markup=reply_admin_menu_markup)

 

                


async def unpost_post_message(message, bot: AsyncTeleBot):
    await bot.set_state(message.from_user.id, MyStates.wait_for_message, message.chat.id)

async def start_gift_process(message, bot: AsyncTeleBot):
   await bot.set_state(message.from_user.id, MyStates.wait_for_user_name, message.chat.id)
   await bot.send_message(message.chat.id, "Введите имя пользователя @username")

async def get_user_name(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    username = message.text.replace('@','')

    async with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["username"]=username

    reply_gift_markup = InlineKeyboardMarkup()
    reply_gift_markup.add(*getProductGift())
    await bot.set_state(message.from_user.id, MyStates.send_gift, message.chat.id)
    await bot.send_message(message.chat.id, "Выберите тип услуги:", reply_markup=reply_gift_markup)


async def send_report(message, bot: AsyncTeleBot):
    user_id = message.chat.id
    text = f"Отчёт на {datetime.datetime.today()}"

    start_date = datetime.datetime.today() - datetime.timedelta(days=31)
    end_date = datetime.datetime.today()
    
    invoices_month_report = generate_invoice_report(start_date, end_date)
    transactions_month_report = generate_transactions_report(start_date, end_date)
    ledger_month_report = generate_ledger_report(start_date, end_date)
    

    await bot.send_document(user_id, InputFile(invoices_month_report), caption = "Отчёт по счетам")
    await bot.send_document(user_id, InputFile(transactions_month_report), caption = "Отчёт по транзакциям")
    await bot.send_document(user_id, InputFile(ledger_month_report), caption = "Общий учет")


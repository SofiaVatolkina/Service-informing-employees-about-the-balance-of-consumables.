import telebot
from telebot import types

class TG:
	"""
	It's static class for connecting to telegram bot.

	This class have __init__ method only for pass settings to this class.
	"""
	bot = None
	callback_function = None

	list_of_consumables_btn = list()
	list_of_service_btn = list()

	def __init__(self, api_key, consumables_list, service_list, callback_function):
		"""
		* 'api_key': is API KEY for your TG bot.
		* 'consumables_list': it's list with list of consumables buttons names.
		* 'service_list': it's list with service buttons names.
		* 'callback_function': it's function for return and processing user messages.
		"""
		if not TG.bot:
			TG.bot = telebot.TeleBot(api_key)
		if not TG.callback_function:
			TG.callback_function = callback_function
		TG.list_of_consumables_btn = consumables_list
		TG.list_of_service_btn = service_list

	@staticmethod
	def bot_start():
		if TG.bot:
			@TG.bot.message_handler(commands=['start', 'help'])
			def send_welcome(message):
				# ONLY write message to user.
					TG.bot.reply_to(message, 'Привет, напиши расходник, информацию о котором ты хочешь получить.')

			@TG.bot.message_handler()
			def chose_consumables(message):
				search_result = ''
				markup = types.ReplyKeyboardMarkup(row_width=1)

				if message.text == 'Выбор популярных расходников':
					# Write buttons from list to markup.
					markup.add(*[types.KeyboardButton(name) for name in TG.list_of_consumables_btn])
				else:
					# Write buttons from list to markup.
					markup.add(*[types.KeyboardButton(name) for name in TG.list_of_service_btn])
					# Pass user message to main.py
					if TG.callback_function:
						search_result = TG.callback_function(message)
					else:
						raise ValueError('callback_function in TG class can not be None!')
				# Write message to user and init menu.
				if search_result:
					TG.bot.send_message(message.from_user.id,
										f'Вот что я нашёл в базе данных: {search_result}.',
										reply_markup=markup)
					print(f'DEBUG: {search_result}')
				else:
					TG.bot.send_message(message.from_user.id,
										'Привет, напиши расходник, информацию о котором ты хочешь получить.',
										reply_markup=markup)

			TG.bot.polling(none_stop=True, interval=5)
		else:
			raise ValueError('Bot is not initialized!')

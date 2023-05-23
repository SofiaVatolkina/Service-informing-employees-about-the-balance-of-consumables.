import telebot
from telebot import types

class TG:
	"""
	It's static class for connecting to telegram bot.

	This class have __init__ method only for pass settings to this class.
	"""
	bot = None

	list_of_consumables_btn = list()
	list_of_service_btn = list()


	def __init__(self, api_key, consumables_list, service_list):
		"""
		* 'api_key': is API KEY for your TG bot.
		* 'consumables_list': it's list with list of consumables buttons names.
		* 'service_list': it's list with service buttons names.
		"""
		TG.bot = telebot.TeleBot(api_key)
		TG.list_of_consumables_btn = consumables_list
		TG.list_of_service_btn = service_list


		@TG.bot.message_handler(commands=['start', 'help'])
		def send_welcome(message):
			# ONLY write message to user.
			TG.bot.reply_to(message, 'Привет, напиши расходник, информацию о котором ты хочешь получить.')

		@TG.bot.message_handler()
		def chose_consumables(message):
			markup = types.ReplyKeyboardMarkup(row_width=1)

			if message.text == 'Выбор популярных расходников':
				# Write buttons from list to markup.
				markup.add(*[types.KeyboardButton(name) for name in TG.list_of_consumables_btn])
			else:
				# Write buttons from list to markup.
				markup.add(*[types.KeyboardButton(name) for name in TG.list_of_service_btn])
			# Write message to user and init menu.
			TG.bot.send_message(message.from_user.id,
										 'Привет, напиши расходник, информацию о котором ты хочешь получить.',
										 reply_markup=markup)

		TG.bot.polling(none_stop=True, interval=5)

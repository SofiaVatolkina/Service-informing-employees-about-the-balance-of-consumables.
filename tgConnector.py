import telebot
from telebot import types

class TG:
	bot = None

	list_of_consumables_btn = list()
	list_of_service_btn = list()

	list_of_consumables_btn.append('масло')
	list_of_consumables_btn.append('бензин')
	list_of_consumables_btn.append('гайки')
	list_of_consumables_btn.append('бобры')
	list_of_service_btn.append('/start')
	list_of_service_btn.append('Выбор популярных расходников')


	def __init__(self, api_key, consumables_file, service_file):
		"""
		* 'api_key': is API KEY for your TG bot.
		* 'consumables_file': is filename with list of consumables buttons names.
		* 'service_file': is filename with service buttons names.
		"""
		self.api_key = api_key
		self.consumables_file = consumables_file
		self.service_file = service_file

		TG.bot = telebot.TeleBot(self.api_key)


		@TG.bot.message_handler(commands=['start', 'help'])
		def send_welcome(message):
			# ONLY write message to user.
			TG.bot.reply_to(message, "Привет, напиши расходник, информацию о котором ты хочешь получить.")

		@TG.bot.message_handler()
		def chose_consumables(message):
			markup = types.ReplyKeyboardMarkup(row_width=1)

			if message.text == "Выбор популярных расходников":
				# Write buttons from list to markup.
				markup.add(*[types.KeyboardButton(name) for name in TG.list_of_consumables_btn])
			else:
				# Write buttons from list to markup.
				markup.add(*[types.KeyboardButton(name) for name in TG.list_of_service_btn])
			# Write message to user and init menu.
			TG.bot.send_message(message.from_user.id,
										 "Привет, напиши расходник, информацию о котором ты хочешь получить.",
										 reply_markup=markup)

		TG.bot.polling(none_stop=True, interval=5)

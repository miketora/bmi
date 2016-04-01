#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-


from telegram import Updater
import logging
import telegram

calc=[]
peso = 0
altezza = 0
operazione = []
weight_category = []
nome = []

logging.basicConfig(
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		level=logging.DEBUG)

logger = logging.getLogger(__name__)

def messaggi_in_arrivo(bot, update):
	global calc
	global peso
	global altezza
	global operazione
	global nome

	if calc==1: 
            try:
                peso = float(update.message.text)
            except ValueError:
                bot.sendMessage(update.message.chat_id,'Give me a number for weight (kg), please.')
                return

            text = "Enter your height (cm)"
            bot.sendMessage(update.message.chat_id, text)
            calc=2

	elif calc==2:
            try:
                altezza = float(update.message.text)
                altezza1 = (altezza/100)
            except ValueError:
                bot.sendMessage(update.message.chat_id,'Give me a number for height (cm), please.')
                return
            calc=0
            imc=int(peso/altezza1**2)

            if imc < 16.5:
                 weight_category = "severely underweight (less than 16.5)"
            elif imc < 18.5:
                 weight_category = "underweight (from 16.5 to 18.4)"
            elif imc < 25:
                 weight_category = "normal (from 18.5 to 24.9)"
            elif imc < 30.1:
                 weight_category = "overweight (from 25 to 30)"
            elif imc < 35:
                 weight_category = "obese class I (from 30.1 to 34.9)"
            elif imc <= 40:
                weight_category = "obese class II (from 35 to 40)"
            else:
                weight_category = "obese class III (over 40)"


            bot.sendMessage(update.message.chat_id,'Hello ' + str(nome) + '\n Your BMI:  ' + str(imc) + '\n BMI Category: ' + str(weight_category) + '\n Weight: ' + str(peso) + " kg" +  '\n Height : ' + str(altezza) + " cm")

	return

def comando_calc(bot, update):
	global calc
	global nome
	calc = 1
	nome = update.message.from_user.first_name
	text= "Enter your weight (kg)"
	bot.sendMessage(update.message.chat_id, text)

def lista(bot, update):
	bot.sendMessage(update.message.chat_id,'\n /start: start bot bmi ' + '\n /info: info bot bmi' + '\n /bmi: start bot bmi' + '\n /list: list command')

def info(bot, update):
	bot.sendMessage(update.message.chat_id,'\n BMI: ' + '\n The body mass index (BMI) or Quetelet index is a value derived from the mass (weight) and height of an individual. The BMI is defined as the body mass divided by the square of the body height, and is universally expressed in units of kg/m2, resulting from mass in kilograms and height in metres.  Wikipedia')

TOKEN = sys.argv[1]

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.addTelegramMessageHandler(messaggi_in_arrivo)
dispatcher.addTelegramCommandHandler("bmi",comando_calc)
dispatcher.addTelegramCommandHandler("start",comando_calc)
dispatcher.addTelegramCommandHandler("list",lista)
dispatcher.addTelegramCommandHandler("info",info)
updater.start_polling()
updater.idle()

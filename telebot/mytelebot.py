import os
import telebot

API_KEY = '7296146723:AAHPWuTR1HRnS_yRSzQEv2gnsT3CY467qyM'
if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I am a bot that will help you monitor your services")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "If you need help, you should ask for it on Google!!")
    
@bot.message_handler(commands=['status'])
def status_command(message):
    LOG_FILE = 'C:\\Users\\Sakuragi Hanamichi\\Documents\\Pt Asyst\\CODE-Uuid\\logs\\app.log'
    error_lines = get_log_status(LOG_FILE)
    
    if error_lines:
        status_message = f'Current Error Status ({len(error_lines)} errors found):\n'
        status_message += '\n'.join(error_lines)
    else:
        status_message = 'No errors found in the log.'
    
    bot.send_message(message.chat.id, status_message)

def get_log_status(log_file_path):
    error_lines = []
    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                if 'ERROR' in line:
                    error_lines.append(line.strip())
    except FileNotFoundError:
        print(f'Error: Log file {log_file_path} not found.')
    except Exception as e:
        print(f'Error reading log file: {str(e)}')
    
    return error_lines

bot.polling()

import os
from telegram.ext import Application, MessageHandler, filters, ChatMemberHandler

# রেলওয়ে ভেরিয়েবল অনুযায়ী TOKEN সেট করা হয়েছে
TOKEN = os.environ.get('TOKEN')

def main():
    app = Application.builder().token(TOKEN).build()
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

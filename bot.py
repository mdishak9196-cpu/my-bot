import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ChatMemberHandler

async def welcome_member(update: Update, context):
    result = update.chat_member
    if result.old_chat_member.status == "left" and result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        chat_title = update.effective_chat.title
        welcome_text = f"হ্যালো {user.mention_markdown_v2()}! {chat_title} গ্রুপে আপনাকে স্বাগতম\\!"
        keyboard = [[InlineKeyboardButton("Join Our Channel ✈️", url="https://t.me/telegram")]]
        await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text, parse_mode='MarkdownV2', reply_markup=InlineKeyboardMarkup(keyboard))

async def filter_links(update: Update, context):
    user_status = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
    if user_status.status in ['administrator', 'creator']: return
    if "http://" in update.message.text.lower() or "https://" in update.message.text.lower() or "t.me/" in update.message.text.lower():
        try:
            await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"⚠️ {update.effective_user.mention_html()}, গ্রুপে লিংক শেয়ার করা নিষিদ্ধ!", parse_mode='HTML')
        except: pass

def main():
    # এখানে আপনার বটের টোকেন এনভায়রনমেন্ট ভেরিয়েবল থেকে নেওয়া হচ্ছে
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print("Error: BOT_TOKEN is not set.")
        return
    app = Application.builder().token(TOKEN).build()
    app.add_handler(ChatMemberHandler(welcome_member, ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_links))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

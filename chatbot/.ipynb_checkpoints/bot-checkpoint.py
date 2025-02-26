from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_pyb as tk
import gemini
TOKEN = '7536532972:AAErpPQ46IPTMxA_TGZi5yzyLRPEZGaTlpA'

# TRIGGER_WORDS = {
#     "안녕" : "안녕하세요!!😊",
#     "정보":"어떤 정보가 필요하세요??",
#     "뭐" : "네?"
# }

async def start(update,context):
    await update.message.reply_text("안녕하세요! 저는 샘봇 입니다. 무엇을 도와드릴까요?")

async def send_photo(update, context):
    photo_url = "https://mblogthumb-phinf.pstatic.net/MjAyMjEyMjhfOTQg/MDAxNjcyMjA0NjM0OTU0.b-D4EcHb6aJI282fr2TqYy3Yzj55SsP_zBh5SAdGKF4g.2_GWgPJzJ2zSP3o_WZA9bmBAlrwcr7ncMJCmKC-Q5K4g.JPEG.sosohan_n/78CA7FC2-DE5F-4DAF-A399-0B1D336AB0AF.jpg?type=w800" # 사진 보내기
    await update.message.reply_photo(photo=photo_url,caption="사진 이미지 불러왔어요") # 사진 보낼 때 같이 딸려오는 꼬리표

async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메세지들
    chat_id = update.message.chat_id # 메세지가 온 채팅방

    if "짱구야" in user_text:
        res = gemini.aiai(user_text.replace("짱구야 ",""))
        await context.bot.send_message(chat_id = chat_id, text = res)
    elif "영화정보" in user_text:pass
        # await 영화정보크롤링() 함수를 실행
    elif "사진줘" in user_text:
        await send_photo(update,context)
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id = chat_id, text = res)
                break # 한개의 키워드에만 반응

def main():
    app = Application.builder().token(TOKEN).build()
    # 명령어 핸들러 추가
    app.add_handler(CommandHandler("start",start))
    # 응답 핸들러 추가
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,monitor_chat)) # 물결은 반대라는 말(TEXT는 하는데 COMMAND는 하지마라는 뜻)    
    
    print("텔레그램 봇이 실행중입니다.모니터링 중...")
    app.run_polling()

if __name__ == '__main__':
    main()
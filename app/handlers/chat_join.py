from aiogram import Router, Bot, F
from aiogram.enums import ChatType
from aiogram.types import ChatJoinRequest, Message

from app.models import dto


async def chat_join_handler(chat_join_request: ChatJoinRequest, bot: Bot):
    await bot.send_message(
        chat_id=chat_join_request.from_user.id,
        text="В каком городе проходит Схватка?"
    )


async def correct_answer(m: Message, user: dto.User, bot: Bot, shvatka_chat_id: int):
    await bot.approve_chat_join_request(chat_id=shvatka_chat_id, user_id=user.tg_id)
    await m.answer("Верно! Вы допущены в чат. До встречи на игре")


def setup(shvatka_chat_id: int) -> Router:
    router = Router(name=__name__)
    router.chat_join_request(chat_join_handler, F.chat.id == shvatka_chat_id)
    router.message(correct_answer, F.chat.type == ChatType.PRIVATE, F.text.lower().conains("лыткарино"))
    return router

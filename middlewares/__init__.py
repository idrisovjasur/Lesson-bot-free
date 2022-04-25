from aiogram import Dispatcher
from middlewares.chekcub import Middlecheck
from loader import dp
from .throttling import ThrottlingMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Middlecheck())

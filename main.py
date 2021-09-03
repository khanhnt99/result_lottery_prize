#!/usr/bin/env python3
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

with open("data.txt", "r") as f:
    result = f.read()
result = result.split(" ")[1:]


def display_lottery_result(update, context):
    display = """
    Đặc biệt            {}
    Nhất                {}
    Nhì             {}      {}
    Ba          {}      {}      {}
                {}      {}      {}
    Tư      {}      {}      {}      {}
    Năm         {}      {}      {}
                {}      {}      {}
    Sáu         {}      {}      {}
    Bảy        {}      {}      {}      {}
    """.format(
        *result
    )
    update.message.reply_text(display)


def compare_result(update, context):
    input_number = int(context.args[0])
    result_numbers = []
    for result_prize in result:
        result_numbers.append(int(result_prize[-2:]))
    if input_number in result_numbers:
        update.message.reply_text("So {} trung giai".format(input_number))
    else:
        update.message.reply_text("Khong trung giai nao\n")
        display_lottery_result()


def how_to_use(update, context):
    direction = """/display: hien thi ket qua so xo\n/compare <number>: xem so lua chon trung giai hay chua
    """
    update.message.reply_text(direction)


def main():
    updater = Updater(token="TOKENACCESS")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("display", display_lottery_result))
    dp.add_handler(CommandHandler("compare", compare_result))
    dp.add_handler(CommandHandler("help", how_to_use))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

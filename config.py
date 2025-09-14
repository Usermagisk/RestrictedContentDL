# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/Rajasthani_ComebackAgain

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count("8262040943:AAEWDhKDFgXtxvafmDxwgNpzlU0CAFrdQ1g") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "BQDdLXsAIFZmJOFQ0gnKrCJVF15k4XnLsqyJFAtx7zQFF5ed5Gw3LVEyKM-o_dV4Vzl6L9FA5vOh9wDf3YwMYsSjkJghvWJbVnAQZTB5xzhVAWrCZlyWbsMywhqqHbRVNXLiK0LGwtYTxAHseaRgoFt0Hy7_j4ekLnbhONfRZtIHFR6LBq3As-lOUO47SGNCaqc2BRcH5LUm1kzfhm2c-WHEGsuF6AS2WLb_f6raXTfy5PxmYG6DFau4aZ1SAbXMrlZ0MGFnVpFxHiy_5COQ0e7r1Rd0YnKepSyMST7-6VbiLKsIsLG6euiaqhB8FaPGoJcvpXzKamhaFAuwNoJ_vL1oIRx5cgAAAAF5pIRyAA"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("API_ID", "14495099"))
    API_HASH = getenv("API_HASH", "2c54ae09ead43077fe57b7ce84cc0f18")
    BOT_TOKEN = getenv("BOT_TOKEN")
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()

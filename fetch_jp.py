import os
import pandas as pd
import yfinance as yf

CODES = CODES = [
    # 原有 14 个（顺序不变）
    "6501","6503","6504","6508","6622","5803","5801","5802","7011","1942",
    "8473","5016","4385","1306",
    # 新增 64 个
    "7203","7974","7013","8306","8035","3542","9434","7261","7270","8061",
    "8601","5185","4755","7012","6203","9984","4665","7201","219A","6809",
    "6857","4063","3444","8136","6954","4502","4005","9005","2702","8053",
    "8001","278A","2986","7746","6616","6481","1605","9882","5947","4732",
    "4503","9503","9436","4528","9989","8766","5108","7267","1928","2914",
    "9433","8316","4452","8593","8058","9278","9104","9501","3103","285A",
    "6166","5019","9508","5401",
]
rows = []
for c in CODES:
    df = yf.Ticker(f"{c}.T").history(period="4mo", interval="1d", auto_adjust=False).tail(80)
    for d, r in df.iterrows():
        rows.append([c, d.strftime("%Y-%m-%d"), r.Open, r.High, r.Low, r.Close, int(r.Volume)])
os.makedirs("data", exist_ok=True)
pd.DataFrame(rows, columns=["code","date","open","high","low","close","volume"]).to_csv("data/latest.csv", index=False)
from datetime import datetime, timezone, timedelta
open("data/updated_at.txt", "w").write(datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M"))

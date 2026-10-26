import os
import pandas as pd
import yfinance as yf

CODES = ["6501","6503","6504","6508","6622","5803","5801","5802","7011","1942","8473","5016","4385","1306"]
rows = []
for c in CODES:
    df = yf.Ticker(f"{c}.T").history(period="4mo", interval="1d", auto_adjust=False).tail(60)
    for d, r in df.iterrows():
        rows.append([c, d.strftime("%Y-%m-%d"), r.Open, r.High, r.Low, r.Close, int(r.Volume)])
os.makedirs("data", exist_ok=True)
pd.DataFrame(rows, columns=["code","date","open","high","low","close","volume"]).to_csv("data/latest.csv", index=False)
from datetime import datetime, timezone, timedelta
open("data/updated_at.txt", "w").write(datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M"))

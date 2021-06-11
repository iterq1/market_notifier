import asyncio
import datetime

import tinvest as ti

TOKEN_SANDBOX = ''
TOKEN_LIVE = ''


async def get_daily_change_by_figi(client: ti.AsyncClient, figi: str):
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=2)

    res = await client.get_market_candles(figi, yesterday, today, ti.CandleResolution.day)

    prev_candle = res.payload.candles[0]
    curr_candle = res.payload.candles[1]
    prev_close = prev_candle.c
    curr_close = curr_candle.c

    change = (curr_close - prev_close) * 100 / prev_close
    return figi, round(change, 2)


async def main():
    client = ti.AsyncClient(TOKEN_SANDBOX, use_sandbox=True)
    etfs_data = await client.get_market_etfs()
    etfs_figis = {etf_data.figi: etf_data for etf_data in etfs_data.payload.instruments}

    res = await asyncio.gather(*[get_daily_change_by_figi(client, figi) for figi in etfs_figis])
    res = sorted(res, key=lambda ec: ec[1])

    for i in res:
        figi = i[0]
        change = i[1]
        etf_data = etfs_figis[figi]
        print(etf_data.ticker, etf_data.name, change)

    await client.close()


if __name__ == '__main__':
    asyncio.run(main())

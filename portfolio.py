from decimal import Decimal

import tinvest as ti
from datetime import datetime

usd = Decimal('72.13')
eur = Decimal('87.32')


async def get_operations(client: ti.AsyncClient, account_id: str):
    from_ = datetime(2020, 9, 1)
    to_ = datetime(2021, 6, 12)
    res = await client.get_operations(from_, to_, broker_account_id=account_id)
    operations = sorted(res.payload.operations, key=lambda x: x.date)
    sum = 0
    for o in operations:
        sum += o.payment
    print(sum)

    portfolio_res = await client.get_portfolio(broker_account_id=account_id)

    portfolio_total = 0
    for p in portfolio_res.payload.positions:
        currency = p.average_position_price.currency.value

        av_price = p.average_position_price.value
        if p.average_position_price_no_nkd is not None:
            av_price = p.average_position_price_no_nkd.value

        if currency == 'USD':
            portfolio_total += av_price*p.balance * usd
        elif currency == 'EUR':
            portfolio_total += p.average_position_price.value*p.balance * eur
        else:
            portfolio_total += p.average_position_price.value*p.balance

    print(portfolio_total)
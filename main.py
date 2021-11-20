import asyncio

import tinvest as ti

from etfs import get_etfs_daily_change, get_etfs_list
from parser import parse_etf_details
from portfolio import get_operations

TOKEN_SANDBOX = ''
TOKEN_LIVE = 't.IbcZlIY33XZ9K7jGWWKiVfDSN14hD849QulZJRChMX3tkm2klhChU_sb_WstIDEELQVduyiJab63B5bAgIO9hw'

broker_account_id = ''
iis_account_id = ''


def init_async_client(sandbox=True) -> ti.AsyncClient:
    token = TOKEN_SANDBOX if sandbox else TOKEN_LIVE
    return ti.AsyncClient(token, use_sandbox=sandbox)


test_url = 'https://www.tinkoff.ru/invest/etfs/TFNX/structure/details/'


async def main():
    client = init_async_client(sandbox=False)
    # await get_operations(client)
    # await get_etfs_daily_change(client)
    # await get_etfs_list(client)
    await parse_etf_details(test_url)
    await client.close()


def sync_main():
    parse_etf_details(test_url)


if __name__ == '__main__':
    sync_main()
    # asyncio.run(main())

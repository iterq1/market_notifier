import asyncio

import tinvest as ti

from etfs import get_etfs_daily_change
from portfolio import get_operations

TOKEN_SANDBOX = ''
TOKEN_LIVE = ''

broker_account_id = ''
iis_account_id = ''


def init_async_client(sandbox=True) -> ti.AsyncClient:
    token = TOKEN_SANDBOX if sandbox else TOKEN_LIVE
    return ti.AsyncClient(token, use_sandbox=sandbox)


async def main():
    client = init_async_client(sandbox=False)
    await get_operations(client, iis_account_id)
    await client.close()


if __name__ == '__main__':
    asyncio.run(main())

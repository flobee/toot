import asyncio

from toot import config
from typing import Optional
from toot.asynch.http import request, Params

# ------------------------------------------------------------------------------
# Accounts
# https://docs.joinmastodon.org/methods/accounts/
# ------------------------------------------------------------------------------


async def verify_credentials(app, user):
    return await auth_get(app, user, "/api/v1/accounts/verify_credentials")


# ------------------------------------------------------------------------------
# ???
# ------------------------------------------------------------------------------

async def get_instance(domain, /, *, scheme="https"):
    url = "{}://{}/api/v1/instance".format(scheme, domain)
    return await anon_get(url)


async def search_accounts(app, user, query):
    return await auth_get(app, user, '/api/v1/accounts/search', {"q": query})


async def get_status(app, user, id):
    return await auth_get(app, user, f"/api/v1/statuses/{id}")


# ------------------------------------------------------------------------------
# Common
# ------------------------------------------------------------------------------

async def anon_get(url: str, params: Optional[Params] = None):
    response = await request("GET", url, params=params)
    return response


async def auth_get(app, user, path, params: Optional[Params] = None):
    url = app.base_url + path
    # headers = {"Authorization": "Bearer " + user.access_token}
    headers = {"Authorization": "Bearer bear"}
    response = await request("GET", url, params=params, headers=headers)
    return response

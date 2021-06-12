import asyncio
import logging

from aiohttp import ClientSession
from dataclasses import dataclass

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class Service:
    name: str
    url: str


SERVICES = [
    Service("users", USERS_DATA_URL),
    Service("posts", POSTS_DATA_URL),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)
    return result


async def get_users() -> str:
    task_result = ""

    tasks = {
        asyncio.create_task(fetch_ip(SERVICES[0]))
    }

    coro = asyncio.wait(
        tasks,
        timeout=2,
        return_when=asyncio.FIRST_COMPLETED
    )

    done, pending = await coro

    for task in pending:
        task.cancel()

    for task in done:
        task_result = task.result()
        break

    return task_result


async def get_posts() -> str:
    task_result = ""

    tasks = {
        asyncio.create_task(fetch_ip(SERVICES[1]))
    }

    coro = asyncio.wait(
        tasks,
        timeout=2,
        return_when=asyncio.FIRST_COMPLETED
    )

    done, pending = await coro

    for task in pending:
        task.cancel()

    for task in done:
        task_result = task.result()
        break

    return task_result

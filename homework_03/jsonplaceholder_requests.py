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
    task_result = await asyncio.create_task(fetch_ip(SERVICES[0]))
    return task_result


async def get_posts() -> str:
    task_result = await asyncio.create_task(fetch_ip(SERVICES[1]))
    return task_result

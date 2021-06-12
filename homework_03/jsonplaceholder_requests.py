import asyncio
import logging

from aiohttp import ClientSession
from dataclasses import dataclass

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

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
    logging.info(f'Fetch ip from {service.name}')

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logging.info(f'Fetched {service.name}. Result: {result}')

    return result


async def get_users() -> str:
    logging.info("Start getting my users")
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
        logging.info(f"Cancelled task {task}")

    for task in done:
        task_result = task.result()
        break
    else:
        logging.warning("Could not fetch users!")

    logging.info("Finish getting my users")
    return task_result


async def get_posts() -> str:
    logging.info("Start getting my posts")
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
        logging.info(f"Cancelled task {task}")

    for task in done:
        task_result = task.result()
        break
    else:
        logging.warning("Could not fetch posts!")

    logging.info("Finish getting my posts")
    return task_result

def main():
    users = asyncio.run(get_users())
    posts = asyncio.run(get_posts())
    logging.info(f"RESULT: {users}")
    logging.info(f"RESULT: {posts}")


if __name__ == '__main__':
    main()
import asyncio

from models import engine, Base, Session, User, Post
from jsonplaceholder_requests import get_posts, get_users
from sqlalchemy import select


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def load_data():
    return await asyncio.gather(
        get_posts(),
        get_users()
    )


async def save_user_in_db(users):
    async with Session() as session:

        async with session.begin():
            for user in users:
                user_model = User(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email'],
                )
                session.add(user_model)


async def save_posts_in_db(posts):
    async with Session() as session:

        async with session.begin():
            for post in posts:
                post_model = Post(
                    id=post['id'],
                    title=post['title'],
                    body=post['body'],
                    user_id=post['userId']
                )
                session.add(post_model)


async def async_main():
    await create_tables()
    posts, users = await load_data()
    await save_user_in_db(users)
    await save_posts_in_db(posts)

def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

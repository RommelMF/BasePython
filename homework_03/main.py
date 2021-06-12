import asyncio

from models import engine, Base, Session, User, Post
from jsonplaceholder_requests import get_posts, get_users


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def load_data():
    return await asyncio.gather(
        get_posts(),
        get_users()
    )


async def save_data_in_db(data):
    async with Session() as session:

        async with session.begin():
            posts = data[0]
            users = data[1]
            for user in users:
                user_model = User(
                    id=user['id'],
                    name=user['name'],
                    username=user['username'],
                    email=user['email'],
                )
                user_model.posts = []
                user_posts = filter(lambda x: x['userId'] == user['id'], posts)
                for post in user_posts:
                    post_model = Post(
                        id=post['id'],
                        title=post['title'],
                        body=post['body'],
                    )
                    user_model.posts.append(post_model)
                session.add(user_model)


async def async_main():
    await create_tables()
    data = await load_data()
    await save_data_in_db(data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

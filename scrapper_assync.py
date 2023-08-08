from aiohttp import ClientSession
from asyncio import gather, get_event_loop, ensure_future

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def run():
    tasks = []
    async with ClientSession() as session:
        for character_id in range(1, 827):
            task = ensure_future(
                fetch(
                    session,
                    f"https://rickandmortyapi.com/api/character/{character_id}"
                )
            )
            tasks.append(task)  # Append the task to the tasks list

        responses = await gather(*tasks)  # Awaiting all tasks in the tasks list
        for resp in responses:
            print(resp["id"], resp["name"], resp["status"], resp["species"], resp["origin"]["name"], resp["image"])


loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)

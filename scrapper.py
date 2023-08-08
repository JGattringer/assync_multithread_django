from aiohttp import ClientSession
from asyncio import gather, get_event_loop, ensure_future
from rickandmortyapp.models import Character
from asgiref.sync import sync_to_async  # Import the sync_to_async function

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

# Define a coroutine function for the asynchronous saving of a character
@sync_to_async
def save_character_async(character):
    character.save()

async def save_character_data(session, url):
    character_data = await fetch(session, url)
    character = Character(
        name=character_data["name"],
        status=character_data["status"],
        species=character_data["species"],
        origin_name=character_data["origin"]["name"],
        image=character_data["image"]
    )
    await save_character_async(character)  # Save asynchronously

async def run():
    tasks = []
    async with ClientSession() as session:
        for character_id in range(1, 827):
            task = ensure_future(
                save_character_data(
                    session,
                    f"https://rickandmortyapi.com/api/character/{character_id}"
                )
            )
            tasks.append(task)

        await gather(*tasks)

loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)

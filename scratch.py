import asyncio

class Qwe:
    def __await__(self):
        yield  # None or yield from [object with feature interface]
        return 1

async def main():
    q = Qwe()
    await q

asyncio.run(main())

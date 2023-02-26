import asyncio
from classes.Interface import Interface

async def main():    
    interface = Interface()
    await interface.chat()

if __name__ == "__main__":
    asyncio.run(main())

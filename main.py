#!/usr/bin/env python3
import asyncio
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()

async def main() -> None:
    print("yo")

if __name__ == "__main__":
    asyncio.run(main())

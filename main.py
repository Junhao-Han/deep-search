#!/usr/bin/env python3
import asyncio
import coordinator

from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
from coordinator import ReserchCoordinator

load_dotenv()

console = Console()

async def main() -> None:
    console.print("[bold cyan]Deep Research Tool[/bold cyan] - Console Edition")
    console.print("This tool performs in-depth research on any topic using AI agents.")

    # User input for the research topic
    query = Prompt.ask("\n[bold]What would you like to research?[/bold]")
    if not query.strip():
        console.print("[bold red]Error:[/bold red] Please provide a valid query.")
        return
    
    research_coordinator = ReserchCoordinator(query)
    report = await research_coordinator.research()

    print(report)

if __name__ == "__main__":
    asyncio.run(main())

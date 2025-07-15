import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt

from coordinator import ResearchCoordinator

load_dotenv()

console = Console()

async def main() -> None:
    # Print the welcome message
    console.print("[bold cyan]Deep Research Tool[/bold cyan] - Console Edition")
    console.print("This tool performs in-depth research on any topic using AI agents.")

    # get the users query
    query = Prompt.ask("\n[bold]What would you like to research?[/bold]")

    # Validate the query
    if not query.strip():
        console.print("[bold red]Error:[/bold red] Please provide a valid query.")
        return
    
    # Start the research process
    research_coordinator = ResearchCoordinator(query)
    report = await research_coordinator.research()

if __name__ == "__main__":
    asyncio.run(main()) 
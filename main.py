from planner import PlannerAgent
from search_agent import SearchAgent
from analyst import AnalystAgent
from writer import WriterAgent


def main():

    print("=" * 50)
    print("     Multi-Agent AI System using Tavily")
    print("=" * 50)

    # User Input
    query = input("\nEnter your topic: ")

    # Create Agent Objects
    planner = PlannerAgent()
    search = SearchAgent()
    analyst = AnalystAgent()
    writer = WriterAgent()

    # Planner Agent
    plan = planner.plan(query)

    # Search Agent
    search_results = search.search(plan["topic"])

    # Analyst Agent
    summary = analyst.analyze(search_results)

    # Writer Agent
    final_report = writer.write(plan["topic"], summary)

    # Display Final Report
    print(final_report)


if __name__ == "__main__":
    main()

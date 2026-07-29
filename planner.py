class PlannerAgent:
    """
    Planner Agent
    Creates an execution plan based on the user's query.
    """

    def plan(self, query):
        print("\n📌 Planner Agent")
        print("Analyzing the user request...")

        plan = {
            "topic": query,
            "steps": [
                "Search information using Tavily",
                "Analyze search results",
                "Generate final report"
            ]
        }

        print("Plan Created Successfully!\n")
        return plan

class WriterAgent:
    """
    Writer Agent
    Generates the final report.
    """

    def write(self, topic, summary):
        print("\n✍️ Writer Agent")
        print("Generating Final Report...\n")

        report = f"""
========================================
            FINAL REPORT
========================================

Topic:
{topic}

Summary:
"""

        for item in summary:
            report += item + "\n"

        report += "\n✅ Report Generated Successfully."

        return report

from utils import extract_text_from_pdf
from agents import analyzer_agent, summary_agent, citation_agent, insights_agent
from reviewer import review_output

MAX_RETRIES = 2

def run_with_review(agent_func, text):
    retries = 0
    while retries < MAX_RETRIES:
        output = agent_func(text)
        score, feedback = review_output(output)

        print(f"Score: {score}")

        if score >= 7:
            return output
        retries += 1

    return output


def main():
    file_path = "sample.pdf"  # upload your paper

    text = extract_text_from_pdf(file_path)

    print("\n--- Analyzer ---")
    analysis = run_with_review(analyzer_agent, text)

    print("\n--- Summary ---")
    summary = run_with_review(summary_agent, text)

    print("\n--- Citations ---")
    citations = run_with_review(citation_agent, text)

    print("\n--- Insights ---")
    insights = run_with_review(insights_agent, text)

    final_report = f"""
    ==========================
    RESEARCH BRIEF
    ==========================

    ANALYSIS:
    {analysis}

    SUMMARY:
    {summary}

    CITATIONS:
    {citations}

    INSIGHTS:
    {insights}
    """

    print(final_report)


if __name__ == "__main__":
    main()

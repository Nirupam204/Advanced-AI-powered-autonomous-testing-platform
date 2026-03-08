from agents.explorer_agent import explore_website
from agents.planner_agent import intelligent_planner
import json

def run_system(url):

    print("\nExploring website...")
    page_data = explore_website(url)

    print("Generating AI strategy...")

    strategy = intelligent_planner(
    url,
    page_data["title"],
    page_data["forms"],
    page_data["password_fields"],
    page_data["load_time"]
)

    print("\nPlanner Strategy:")
    print(json.dumps(strategy, indent=4))


if __name__ == "__main__":

    while True:

        url = input("Enter URL (or type exit): ")

        if url.lower() == "exit":
            break

        try:
            run_system(url)
            print("\n" + "-"*40 + "\n")

        except Exception as e:
            print("Error:", e)
            
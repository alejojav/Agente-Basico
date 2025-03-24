import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily_search_tool = TavilySearchResults(
    max_results=2,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=False,
    include_images=False,
)

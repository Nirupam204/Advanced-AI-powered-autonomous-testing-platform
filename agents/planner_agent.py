from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import json
import re

def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError("No valid JSON found")


def intelligent_planner(url, title, forms, password_fields, load_time):
    llm = OllamaLLM(
        model="phi3",
        temperature=0.2,
        format="json"
    )

    prompt = ChatPromptTemplate.from_template("""
You are a senior QA architect AI system.

Analyze the website metadata carefully and generate an adaptive crawl strategy.

Website URL: {url}
Page Title: {title}
Number of Forms: {forms}
Number of Password Fields: {password_fields}
Page Load Time (ms): {load_time}

Think internally before deciding.
Do not explain your reasoning.
Return ONLY valid JSON.

Required format:

{{
  "requires_auth": true or false,
  "crawl_depth": number between 1 and 10,
  "prioritize_forms": true or false,
  "key_focus_area": "accessibility" or "performance" or "navigation"
}}
""")

    chain = prompt | llm
    response = chain.invoke({
    "url": url,
    "title": title,
    "forms": forms,
    "password_fields": password_fields,
    "load_time": load_time
})

    return extract_json(response)

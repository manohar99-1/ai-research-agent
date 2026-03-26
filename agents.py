from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def analyzer_agent(text):
    prompt = f"""
    Extract:
    - problem
    - methodology
    - experiments
    - findings
    
    Paper:
    {text[:8000]}
    
    Return JSON.
    """
    return llm.predict(prompt)

def summary_agent(text):
    prompt = f"""
    Summarize this paper in 150-200 words:
    {text[:8000]}
    """
    return llm.predict(prompt)

def citation_agent(text):
    prompt = f"""
    Extract all citations/references from:
    {text[-5000:]}
    """
    return llm.predict(prompt)

def insights_agent(text):
    prompt = f"""
    Give key insights and applications:
    {text[:8000]}
    """
    return llm.predict(prompt)

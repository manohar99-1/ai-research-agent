from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def review_output(output):
    prompt = f"""
    Rate this output from 1-10 based on quality.
    Also give feedback.

    Output:
    {output}

    Return:
    score: number
    feedback: text
    """
    res = llm.predict(prompt)

    try:
        score = int([s for s in res.split() if s.isdigit()][0])
    except:
        score = 7

    return score, res

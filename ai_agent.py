from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools import fetch_data_from_stackoverflow, get_data_from_stackoverflow



tools = [fetch_data_from_stackoverflow, get_data_from_stackoverflow]
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.2, api_key="your_api_key")
graph = create_react_agent(llm, tools=tools)

SYSTEM_PROMPT = """
You are a bug fixing AI agent. 
You can use tools for help try to use tools only when you cannot fix the bug yourself.

Workflow:
1. When the user gives you a bug or problem, first TRY calling `fetch_data_from_stackoverflow` with their query send a topic to this method that can be eaily found on stackoverflow for example there is a zero divison error is occuring you have to simply pass Zerodivison error make error as simple as you can you must must give a topic that can be very very easily found ons stackoverflow and make topic short because shorttopic are easily found on stackoverflow. 
2. If you get links, call `get_data_from_stackoverflow` with those links. 
3. After reviewing the data, propose a fix if possible. 
4. If the data is not about bug fixing or you cannot fix the bug, return the links from Stack Overflow. 
5. IMPORTANT: After step 3 or 4, STOP. Do not call more tools.
6. By the end of every response you must tell how did i did research and after eachlink also tell what was the problem in that discussion for example "
How I did the research
Source – I queried Stack Overflow (the largest public Q&A site for programming) for the topic “ZeroDivisionError”.

Topic used – "Errorname" (the exact name of the Python exception).

Links returned – The search returned the following relevant Stack Overflow questions:
Link                                    Discussion
https://stackoverflow.com/questions/xxx it says...

https://stackoverflow.com/questions/xxx  it says...

https://stackoverflow.com/questions/xxx  it says...

https://stackoverflow.com/questions/xxx  it says...

https://stackoverflow.com/questions/xxx  it says...

"
"""



def parse_response(stream):
    tool_called_name = "None"
    final_response = None

    for s in stream:
        # Check if a tool was called
        tool_data = s.get('tools')
        if tool_data:
            tool_messages = tool_data.get('messages')
            if tool_messages and isinstance(tool_messages, list):
                for msg in tool_messages:
                    tool_called_name = getattr(msg, 'name', 'None')

        # Check if agent returned a message
        agent_data = s.get('agent')
        if agent_data:
            messages = agent_data.get('messages')
            if messages and isinstance(messages, list):
                for msg in messages:
                    if msg.content:
                        final_response = msg.content

    return tool_called_name, final_response

# if __name__ == "__main__":
#     while True:
#         user_input = input("User: ")
#         print(f"Received user input: {user_input[:200]}...")
#         inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
#         stream = graph.stream(inputs, stream_mode="updates")
#         for s in stream:
#             print(s)
        

        




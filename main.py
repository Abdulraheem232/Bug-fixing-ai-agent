import streamlit as st
from ai_agent import graph, SYSTEM_PROMPT,parse_response

st.title("Bug fixing ai agent")
st.write("This is a bug fixing ai agent it will try to fix bugs in your code and if it cant fix it then it will give you some links from stackoverflow and then it will give you some data from that links and then you can use that data to fix your code.")
user_input = st.text_area("Enter your problem/bug here", height=300)
button_clicked = st.button("Submit", on_click=lambda: st.write("Processing..."))  # Placeholder for button action

if button_clicked:
    # Simulate fetching data from Stack Overflow
    inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", user_input)]}
    stream = graph.stream(inputs)
    tool_called_name,final_response = parse_response(stream)
    st.write("Tool called:", tool_called_name)
    st.write("Final response:", final_response)


    

import streamlit as st
from solver import solve_problem

st.set_page_config(page_title="DSA Problem Solver", layout="wide")
st.title("DSA Problem Solver Agent")
st.write("Enter a problem description and the agent will pick an algorithm and return an explanation, example code, and complexity notes.")

EXAMPLES = [
    "Given a sorted array, find if target exists using binary search",
    "Sort the array of integers in non-decreasing order",
    "Find the Nth Fibonacci number",
    "Given a graph, list nodes reachable from 1 using BFS",
]

with st.sidebar:
    st.header("Examples")
    example_choice = st.selectbox("Choose an example to load", ["-- none --"] + EXAMPLES)
    if st.button("Load example"):
        st.session_state["problem_text"] = example_choice if example_choice != "-- none --" else ""
    st.markdown("---")
    st.markdown("Tips:\n- Be concise and mention keywords like 'binary search', 'sort', 'graph', 'dp'\n- This MVP uses keyword heuristics to pick an algorithm")

if "problem_text" not in st.session_state:
    st.session_state["problem_text"] = ""

problem_text = st.text_area("Problem description", value=st.session_state["problem_text"], height=180)

if st.button("Solve"):
    if not problem_text.strip():
        st.warning("Please enter a problem description or choose an example.")
    else:
        with st.spinner("Solving..."):
            result = solve_problem(problem_text)
        st.subheader("Explanation")
        st.markdown(result.get("explanation", "_No explanation provided._"))
        st.subheader("Complexity")
        st.write(result.get("complexity", "_No complexity info._"))
        st.subheader("Example Code (Python)")
        code = result.get("code", "")
        if code:
            st.code(code, language="python")
            st.download_button("Download code", data=code, file_name="solution.py", mime="text/x-python")
        else:
            st.info("No example code available.")

st.markdown("---")
st.caption("Note: This app shows example solutions and does not execute generated code. Be careful running untrusted code.")

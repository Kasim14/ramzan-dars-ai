import streamlit as st
from notes_manager import save_note, load_notes
from gemini_ai import ask_ai

st.set_page_config(page_title="Ramzan Dars AI", layout="wide")

st.title("Ramzan Dars AI Assistant")

menu = st.sidebar.radio(
    "Menu",
    ["Add Notes", "View Notes", "Ask AI"]
)

# ADD NOTES
if menu == "Add Notes":

    st.header("Add New Dars Notes")

    title = st.text_input("Dars Title")

    content = st.text_area("Write Notes")

    if st.button("Save Notes"):

        save_note(title, content)

        st.success("Notes Saved!")

# VIEW NOTES
elif menu == "View Notes":

    st.header("Saved Notes")

    notes = load_notes()

    for n in notes:

        with st.expander(n["title"]):

            st.write(n["content"])

# ASK AI
elif menu == "Ask AI":

    st.header("Ask AI From Notes")

    notes = load_notes()

    titles = [n["title"] for n in notes]

    # session state for question
    if "question" not in st.session_state:
        st.session_state.question = ""

    with st.form("ask_ai_form"):

        selected = st.multiselect("Select Dars", titles)

        question = st.text_input(
            "Ask Question",
            value=st.session_state.question
        )

        submit = st.form_submit_button("Ask AI")

    # store question in session
    st.session_state.question = question

    if submit:

        selected_notes = ""

        for n in notes:
            if n["title"] in selected:
                selected_notes += n["content"] + "\n"

        if not selected:
            st.warning("Please select at least one Dars")

        elif question.strip() == "":
            st.warning("Please enter a question")

        else:

            answer = ask_ai(selected_notes, question)

            st.subheader("AI Answer")

            st.write(answer)
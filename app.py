import streamlit as st
from notes_manager import load_notes, add_note, update_note, delete_note
from gemini_ai import ask_ai

st.set_page_config(page_title="Ramzan Dars AI", layout="centered")

# session states
if "page" not in st.session_state:
    st.session_state.page = "notes"

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None


# ============================
# NOTES PAGE
# ============================

if st.session_state.page == "notes":

    st.title("Ramzan Dars Notes")

    notes = load_notes()

    for i, n in enumerate(notes):

        col1, col2 = st.columns([8,1])

        with col1:
            with st.expander(n["title"]):
                st.write(n["content"])

        with col2:

            if st.button("⋮", key=f"menu{i}"):

                st.session_state.edit_index = i
                st.session_state.page = "options"
                st.rerun()


    # floating add button
    if st.button("➕ Add Note"):
        st.session_state.page = "editor"
        st.session_state.edit_index = None
        st.rerun()



# ============================
# NOTE EDITOR
# ============================

elif st.session_state.page == "editor":

    st.title("Write Note")

    notes = load_notes()

    title = ""
    content = ""

    if st.session_state.edit_index is not None:

        note = notes[st.session_state.edit_index]
        title = note["title"]
        content = note["content"]

    title = st.text_input("Title", value=title)
    content = st.text_area("Notes", value=content, height=300)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✔ Save"):

            if st.session_state.edit_index is None:
                add_note(title, content)
            else:
                update_note(st.session_state.edit_index, title, content)

            st.session_state.page = "notes"
            st.rerun()

    with col2:
        if st.button("Cancel"):
            st.session_state.page = "notes"
            st.rerun()



# ============================
# OPTIONS MENU
# ============================

elif st.session_state.page == "options":

    st.title("Note Options")

    i = st.session_state.edit_index
    notes = load_notes()

    st.write(notes[i]["title"])

    if st.button("✏ Edit"):
        st.session_state.page = "editor"
        st.rerun()

    if st.button("🗑 Delete"):
        delete_note(i)
        st.session_state.page = "notes"
        st.rerun()

    new_name = st.text_input("Rename")

    if st.button("Rename"):
        update_note(i, new_name, notes[i]["content"])
        st.session_state.page = "notes"
        st.rerun()

    if st.button("Back"):
        st.session_state.page = "notes"
        st.rerun()
# import json

# FILE_PATH = "data/notes.json"

# def load_notes():
#     try:
#         with open(FILE_PATH, "r") as f:
#             return json.load(f)
#     except:
#         return []

# def save_note(title, content):

#     notes = load_notes()

#     notes.append({
#         "title": title,
#         "content": content
#     })

#     with open(FILE_PATH, "w") as f:
#         json.dump(notes, f, indent=4)
import json

FILE = "data/notes.json"

def load_notes():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note(title, content):
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)

def update_note(index, title, content):
    notes = load_notes()
    notes[index]["title"] = title
    notes[index]["content"] = content
    save_notes(notes)

def delete_note(index):
    notes = load_notes()
    notes.pop(index)
    save_notes(notes)
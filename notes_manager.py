import json

FILE_PATH = "data/notes.json"

def load_notes():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def save_note(title, content):

    notes = load_notes()

    notes.append({
        "title": title,
        "content": content
    })

    with open(FILE_PATH, "w") as f:
        json.dump(notes, f, indent=4)
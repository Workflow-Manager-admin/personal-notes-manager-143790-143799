import os
import sqlite3
from flask import g
from datetime import datetime

# PUBLIC_INTERFACE
def get_db():
    """Get a connection to the SQLite database, creating the table if necessary."""
    db = getattr(g, '_database', None)
    if db is None:
        db_path = os.environ.get("NOTES_DB_PATH") or os.path.join(os.path.dirname(__file__), "../../notes.db")
        db = g._database = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        db.row_factory = sqlite3.Row
        create_table_if_not_exists(db)
    return db

def create_table_if_not_exists(db):
    """Create the notes table if it doesn't exist."""
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL
        )
        """
    )
    db.commit()

# PUBLIC_INTERFACE
def close_db(exception=None):
    """Close the database on teardown."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# PUBLIC_INTERFACE
def list_notes():
    """List all notes."""
    db = get_db()
    cur = db.execute('SELECT id, title, content, created_at, updated_at FROM notes ORDER BY created_at DESC')
    return [dict(row) for row in cur.fetchall()]

# PUBLIC_INTERFACE
def get_note(note_id):
    """Get a single note by ID."""
    db = get_db()
    cur = db.execute('SELECT id, title, content, created_at, updated_at FROM notes WHERE id = ?', (note_id,))
    row = cur.fetchone()
    return dict(row) if row else None

# PUBLIC_INTERFACE
def create_note(title, content):
    """Create a new note."""
    db = get_db()
    now = datetime.utcnow()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
        (title, content, now, now)
    )
    db.commit()
    return cursor.lastrowid

# PUBLIC_INTERFACE
def update_note(note_id, title, content):
    """Update an existing note."""
    db = get_db()
    now = datetime.utcnow()
    db.execute(
        "UPDATE notes SET title = ?, content = ?, updated_at = ? WHERE id = ?",
        (title, content, now, note_id)
    )
    db.commit()

# PUBLIC_INTERFACE
def delete_note(note_id):
    """Delete a note by ID."""
    db = get_db()
    db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    db.commit()

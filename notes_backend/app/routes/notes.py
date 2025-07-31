from flask_smorest import Blueprint
from flask.views import MethodView
from flask import abort

from .. import models
from ..schemas import NoteSchema, NoteCreateSchema, NoteUpdateSchema

blp = Blueprint(
    "Notes", "notes", url_prefix="/notes",
    description="CRUD operations for personal notes"
)

@blp.route("/")
class NotesList(MethodView):
    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema(many=True))
    def get(self):
        """List all notes."""
        return models.list_notes()

    # PUBLIC_INTERFACE
    @blp.arguments(NoteCreateSchema)
    @blp.response(201, NoteSchema)
    def post(self, new_data):
        """Create a new note."""
        note_id = models.create_note(new_data["title"], new_data["content"])
        note = models.get_note(note_id)
        return note

@blp.route("/<int:note_id>")
class NoteItem(MethodView):
    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema)
    def get(self, note_id):
        """Retrieve note by ID."""
        note = models.get_note(note_id)
        if not note:
            abort(404, message="Note not found")
        return note

    # PUBLIC_INTERFACE
    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NoteSchema)
    def put(self, update_data, note_id):
        """Update a note by ID."""
        note = models.get_note(note_id)
        if not note:
            abort(404, message="Note not found")
        updated_title = update_data.get('title', note['title'])
        updated_content = update_data.get('content', note['content'])
        models.update_note(note_id, updated_title, updated_content)
        return models.get_note(note_id)

    # PUBLIC_INTERFACE
    def delete(self, note_id):
        """Delete a note by ID."""
        note = models.get_note(note_id)
        if not note:
            abort(404, message="Note not found")
        models.delete_note(note_id)
        return {"message": "Note deleted."}, 204

from marshmallow import Schema, fields

# PUBLIC_INTERFACE
class NoteSchema(Schema):
    id = fields.Int(dump_only=True, description="Note ID")
    title = fields.Str(required=True, description="Note title")
    content = fields.Str(required=True, description="Note content")
    created_at = fields.DateTime(dump_only=True, description="Note creation timestamp")
    updated_at = fields.DateTime(dump_only=True, description="Note last update timestamp")

# PUBLIC_INTERFACE
class NoteCreateSchema(Schema):
    title = fields.Str(required=True, description="Note title")
    content = fields.Str(required=True, description="Note content")

# PUBLIC_INTERFACE
class NoteUpdateSchema(Schema):
    title = fields.Str(required=False, description="Note title")
    content = fields.Str(required=False, description="Note content")

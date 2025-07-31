# personal-notes-manager-143790-143799

## Notes Backend API

A Flask API container for managing personal notes (CRUD operations).

### Usage

1. Place your configuration in `.env` or copy from `.env.example`.
2. Install dependencies:  
   ```
   pip install -r requirements.txt
   ```
3. Start the application:
   ```
   python run.py
   ```

### API Endpoints

- `GET /notes/` — List all notes
- `POST /notes/` — Create a new note (body: `{ "title": "...", "content": "..." }`)
- `GET /notes/<note_id>` — Retrieve a note by ID
- `PUT /notes/<note_id>` — Update a note by ID (partial or full, body: `{ "title": "...", "content": "..." }`)
- `DELETE /notes/<note_id>` — Delete a note by ID

API documentation is available at `/docs`.
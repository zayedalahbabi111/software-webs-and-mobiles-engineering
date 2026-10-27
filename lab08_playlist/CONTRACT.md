# Playlist API contract

Both partners must use these exact paths, field names, bodies, and HTTP status codes.
The server runs at `http://127.0.0.1:8000`; all paths below are relative.
The shared naming style is **snake_case** (all JSON fields are single lowercase words).
Every response body shown below is JSON.

## 1. Get all songs

Method: GET  
Path: `/songs`  
Request body: none  
Response status: 200  
Response body (the three starting songs):

```json
[
  {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
  {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
  {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0}
]
```

The songs are returned in insertion order, including any songs added after startup.

## 2. Add a song

Method: POST  
Path: `/songs`  
Request body:

```json
{"title": "Imagine", "artist": "John Lennon"}
```

Response status: 201  
Response body (example if this is the first new song):

```json
{"id": 4, "title": "Imagine", "artist": "John Lennon", "votes": 0}
```

Error status (title or artist missing or empty): 400  
Error body:

```json
{"error": "Title and artist are required"}
```

Whitespace-only fields are empty; rejected requests do not add songs or use IDs.

## 3. Vote for a song

Method: POST  
Path (song's id written as `{id}`): `/songs/{id}/vote`  
Request body: none  
Response status: 200  
Response body (example of voting once for song 1):

```json
{"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 4}
```

Error status (no song with that id): 404  
Error body (example for id 99999):

```json
{"error": "There is no song 99999"}
```

All error responses follow the same JSON structure: `{"error": "user-readable message"}`.

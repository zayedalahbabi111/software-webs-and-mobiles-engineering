"""Contract regression tests for AI1220 Lab 08.

Run from this folder with: uv run python -m unittest -v test_backend.py
"""
import unittest

from fastapi.testclient import TestClient
from backend import create_app


class PlaylistContractTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(create_app())

    def tearDown(self):
        self.client.close()

    def test_homepage_is_served(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Collaborative Playlist", response.text)

    def test_initial_songs_and_order(self):
        response = self.client.get("/songs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"id": 1, "title": "Blue Monday", "artist": "New Order", "votes": 3},
            {"id": 2, "title": "Clocks", "artist": "Coldplay", "votes": 1},
            {"id": 3, "title": "Dancing Queen", "artist": "ABBA", "votes": 0},
        ])

    def test_add_song_assigns_next_id_and_keeps_order(self):
        response = self.client.post("/songs", json={"title": " Yellow ", "artist": " Coldplay "})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 4, "title": "Yellow", "artist": "Coldplay", "votes": 0})
        self.assertEqual([song["id"] for song in self.client.get("/songs").json()], [1, 2, 3, 4])

    def test_rejected_songs_do_not_change_playlist_or_ids(self):
        invalid = [
            {}, {"title": "", "artist": "A"}, {"title": "   ", "artist": "A"},
            {"title": "A"}, {"title": "A", "artist": "  "},
            {"title": 4, "artist": "A"}, ["not an object"],
        ]
        for body in invalid:
            with self.subTest(body=body):
                response = self.client.post("/songs", json=body)
                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.json(), {"error": "Title and artist are required"})
        self.assertEqual(len(self.client.get("/songs").json()), 3)
        response = self.client.post("/songs", json={"title": "New", "artist": "Artist"})
        self.assertEqual(response.json()["id"], 4)

    def test_vote_increments_one_and_missing_id_is_rejected(self):
        response = self.client.post("/songs/1/vote")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["votes"], 4)
        missing = self.client.post("/songs/99999/vote")
        self.assertEqual(missing.status_code, 404)
        self.assertEqual(missing.json(), {"error": "There is no song 99999"})
        self.assertEqual(self.client.get("/songs").json()[0]["votes"], 4)

    def test_new_app_starts_fresh(self):
        self.client.post("/songs", json={"title": "Extra", "artist": "Artist"})
        with TestClient(create_app()) as fresh:
            self.assertEqual(len(fresh.get("/songs").json()), 3)


if __name__ == "__main__":
    unittest.main()

from typing import Dict, Any
import pytest
import requests


class TestPosts:
    def test_get_posts(self, session: requests.Session, base_url: str) -> None:
        """Check that posts list is returned."""
        r = session.get(f"{base_url}/posts")
        assert r.status_code == 200

        data = r.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert {"userId", "id", "title", "body"}.issubset(data[0].keys())

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id(self, session: requests.Session, base_url: str, post_id: int) -> None:
        """Check that a post can be fetched by id."""
        r = session.get(f"{base_url}/posts/{post_id}")
        assert r.status_code == 200

        item = r.json()
        assert item.get("id") == post_id
        assert {"userId", "id", "title", "body"}.issubset(item.keys())

    def test_create_post(self, session: requests.Session, base_url: str) -> None:
        """Check post creation."""
        payload: Dict[str, Any] = {
            "title": "foo",
            "body": "bar",
            "userId": 1,
        }

        r = session.post(f"{base_url}/posts", json=payload)
        assert r.status_code == 201

        resp = r.json()
        assert resp["title"] == payload["title"]
        assert resp["body"] == payload["body"]
        assert resp["userId"] == payload["userId"]
        assert "id" in resp

    @pytest.mark.parametrize(
        "post_id,new_title",
        [(1, "updated title"), (2, "another title")],
    )
    def test_update_post(
        self,
        session: requests.Session,
        base_url: str,
        post_id: int,
        new_title: str,
    ) -> None:
        """Check post update."""
        payload = {
            "id": post_id,
            "title": new_title,
            "body": "updated",
            "userId": 1,
        }

        r = session.put(f"{base_url}/posts/{post_id}", json=payload)
        assert r.status_code == 200

        resp = r.json()
        assert resp["id"] == post_id
        assert resp["title"] == new_title

    def test_delete_post(self, session: requests.Session, base_url: str) -> None:
        """Check post deletion."""
        r = session.delete(f"{base_url}/posts/1")
        assert r.status_code in (200, 204)

    def test_get_invalid_post(self, session: requests.Session, base_url: str) -> None:
        """Check invalid post request."""
        r = session.get(f"{base_url}/posts/invalid")
        assert r.status_code == 404

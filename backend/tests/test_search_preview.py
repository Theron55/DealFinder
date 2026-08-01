from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_search_preview_accepts_valid_request() -> None:
    response = client.post(
        "/api/v1/searches/preview",
        json={
            "query": "Sony camera for travel videos",
            "max_budget": 700,
            "condition": "used",
            "required_features": [
                "4K video",
                "interchangeable lens",
            ],
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "query": "Sony camera for travel videos",
        "max_budget": 700.0,
        "condition": "used",
        "required_features": [
            "4K video",
            "interchangeable lens",
        ],
    }


def test_search_preview_rejects_negative_budget() -> None:
    response = client.post(
        "/api/v1/searches/preview",
        json={
            "query": "Sony camera",
            "max_budget": -100,
        },
    )

    assert response.status_code == 422


def test_search_preview_rejects_empty_query() -> None:
    response = client.post(
        "/api/v1/searches/preview",
        json={
            "query": "",
            "max_budget": 500,
        },
    )

    assert response.status_code == 422
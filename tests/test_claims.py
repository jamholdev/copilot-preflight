import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True, "DATABASE": str(tmp_path / "test.sqlite")})
    return app.test_client()


def test_health(client):
    assert client.get("/health").get_json() == {"status": "ok"}


def test_get_claim(client):
    body = client.get("/claims/CLM-0001").get_json()
    assert body["status"] == "APPROVED"


def test_missing_claim_404(client):
    assert client.get("/claims/NOPE").status_code == 404


def test_member_claims(client):
    body = client.get("/members/SYN-1001/claims").get_json()
    assert len(body) == 2


def test_member_claims_rejects_injection(client):
    # Parameterized query treats this as a literal string, so nothing matches.
    body = client.get("/members/SYN-1001' OR '1'='1/claims").get_json()
    assert body == []

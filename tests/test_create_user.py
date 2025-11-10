from tests.helpers import assert_json
def test_create_user(api, base_url):
    payload = {"name": "Emma", "job": "Artist"}

    response = api.post(f"{base_url}/users", json=payload)
    print("response", response.status_code, response.text)

    assert response.status_code == 201
    body = assert_json(response)

    # content structure checks
    assert body.get("name") == "Emma"
    assert "id" in body
    assert "createdAt" in body
from tests.helpers import assert_json
def test_list_users_page2(api, base_url):
    # Step 1: send the request
    response = api.get(f"{base_url}/users", params={'page': 2})

    # Step 2: basic sanity checks
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    # Step 3: Parse the JSON
    body = assert_json(response)

    # Step 4: Validate structure
    assert body.get("page") == 2 # Making sure we are in the correct page
    assert "data" in body
    assert isinstance(body.get("data"), list)
    

    # Step 5: Validate content, each user has the essential keys
    users = body["data"]
    for user in users:
        assert "id" in user
        assert "email" in user
        assert user["email"].endswith("@reqres.in")

def test_users_performance(api, base_url, max_ms):
    response = api.get(f"{base_url}/users", params={"page": 2})
    # sanity check
    assert response.status_code == 200
    # Performance: measuring time elapsed
    elapsed_ms = response.elapsed.total_seconds()*1000.0
    assert elapsed_ms < max_ms, f"Slow response: request took {elapsed_ms} ms"

def test_create_user_performance(api, base_url, max_ms):
    payload = {"name": "Emma", "job": "Artist"}
    response = api.post(f"{base_url}/users", json=payload)
    # sanity check
    assert response.status_code == 201
    # Performance: measuring time elapsed
    elapsed_ms = response.elapsed.total_seconds()*1000.0
    assert elapsed_ms < max_ms, f"Slow response: request took {elapsed_ms} ms"
    
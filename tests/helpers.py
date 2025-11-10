def assert_json(response):
    try:
        return response.json()
    except ValueError as e:
        raise AssertionError(
            f"Expected JSON but got: {response.text[:200]}"
        ) from e
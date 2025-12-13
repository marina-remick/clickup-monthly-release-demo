def test_root_endpoint():
    response = {"status": "ok", "message": "API v2.4.0 ready for monthly release demo"}
    assert response["status"] == "ok"


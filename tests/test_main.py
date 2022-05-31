def test_index_page(client):
    response = client.get("/")
    assert b"hello" in response.data

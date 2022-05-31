def test_index_page(client):
    response = client.get("/")
    assert b"hello" in response.data

def test_get_thing(client):
    response = client.get("/db")
    assert b"bar" in response.data

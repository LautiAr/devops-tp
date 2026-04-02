from app import app

def test_health():
    client = app.test_client()
    res = client.get("/health")
    
    assert res.status_code == 200
    assert res.json["status"] == "ok"
    
def test_length():
    client = app.test_client()
    res = client.get("/len/10")
    
    assert res.status_code == 200
    assert len(res.json["password"]) == 10
    
def test_string():
    client = app.test_client()
    res = client.get("/len/abc")
    
    assert res.status_code == 400

def test_zero():
    client = app.test_client()
    res = client.get("/len/0")

    assert res.status_code == 400    
    

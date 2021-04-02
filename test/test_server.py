from hello import app
with app.test_client() as c:
    print("****************************Hello Circle CI***************************")
    response = c.get('/')
    assert response.data == b'Hello World!'
    

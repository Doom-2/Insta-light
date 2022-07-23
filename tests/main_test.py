def test_root_status(test_client) -> None:
    """ Checking whether the desired status code is obtained """
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200, "Status code is wrong"

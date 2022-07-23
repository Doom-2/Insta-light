class TestPost:

    def test_single_post_status(self, test_client):
        """Checking whether the desired status code is obtained """
        response = test_client.get('/posts/5', follow_redirects=True)
        assert response.status_code == 200, "Status code of post page request is wrong"

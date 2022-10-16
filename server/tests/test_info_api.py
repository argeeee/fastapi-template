# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.info import Info  # noqa: F401


def test_get_info(client: TestClient):
    """Test case for get_info

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/info",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


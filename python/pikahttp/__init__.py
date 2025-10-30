from ._core import Session


class Response:
    def __init__(self, response_dict):
        self._response = response_dict
        self.status_code = response_dict["status_code"]
        self.headers = response_dict["headers"]
        self._content = response_dict["content"]

    @property
    def content(self):
        return self._content

    def json(self):
        import json

        return json.loads(self.text)

    @property
    def text(self):
        return self.content.decode("utf-8")


class HTTPClient:
    def __init__(self):
        self.session = Session()

    async def get(self, url, *, headers=None, params=None, timeout=None):
        response = await self.session.get(url, headers, params, timeout)
        return Response(response)

    async def post(
        self, url, *, headers=None, params=None, json=None, data=None, timeout=None
    ):
        response = await self.session.post(url, headers, params, json, data, timeout)
        return Response(response)


def create_client():
    return HTTPClient()


# Create default client instance
default_client = create_client()


# Expose convenience methods that use the default client
async def get(url, **kwargs):
    return await default_client.get(url, **kwargs)


async def post(url, **kwargs):
    return await default_client.post(url, **kwargs)

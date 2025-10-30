from ._core import Session


class Response(dict):
    def __init__(self, response_dict):
        super().__init__(response_dict)
        for key, value in response_dict.items():
            if key != "content":
                setattr(self, key, value)
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


def get(url, **kwargs):
    session = Session()
    response = session.request("GET", url, headers=kwargs.get("headers"), body=None)
    return Response(response)


def post(url, **kwargs):
    import json

    body = None
    if "json" in kwargs:
        body = json.dumps(kwargs["json"])
    elif "data" in kwargs:
        body = kwargs["data"]
    response = Session().request("POST", url, headers=kwargs.get("headers"), body=body)
    return Response(response)


def create_client():
    return HTTPClient()


# Create default client instance
default_client = create_client()


# Expose convenience methods that use the default client
async def aget(url, **kwargs):
    return await default_client.get(url, **kwargs)


async def apost(url, **kwargs):
    return await default_client.post(url, **kwargs)

from pikahttp import Session


def main():
    # Create a session
    session = Session()

    # Set custom headers
    headers = {
        "User-Agent": "pikahttp/0.1.0",
        "Accept": "application/vnd.github.v3+json",
        "X-Custom-Header": "custom value",
    }

    # Make request with custom headers
    response = session.request(
        "GET", "https://api.github.com/users/octocat", headers=headers
    )

    # Print response
    print(f"Status code: {response['status_code']}")
    print("Response headers:")
    print(response.get("headers", {}))
    print(f"\nContent: {response['content'].decode()}")


if __name__ == "__main__":
    main()

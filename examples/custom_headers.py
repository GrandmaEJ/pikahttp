import pikahttp as pika


def main():
    # Set custom headers
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-Custom-Header": "custom value",
    }

    # Make request with custom headers using requests-like API
    response = pika.get("https://api.github.com/users/octocat", headers=headers)

    # Print response
    print(f"Status code: {response.status_code}")
    print("Response headers:")
    print(response.headers)
    print(f"\nContent: {response.text}")


if __name__ == "__main__":
    main()

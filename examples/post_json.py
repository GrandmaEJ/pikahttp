import pikahttp as pika


def main():
    # Set data
    data = {"title": "Test Post", "body": "This is a test post using pikahttp"}

    # Make POST request using requests-like API
    response = pika.post("https://jsonplaceholder.typicode.com/posts", json=data)

    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Response data: {response.json()}")


if __name__ == "__main__":
    main()

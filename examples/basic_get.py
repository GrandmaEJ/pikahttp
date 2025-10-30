import pikahttp as pika


def main():
    # Make GET request using requests-like API
    response = pika.get("https://api.github.com/zen")

    # Print response
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.text}")


if __name__ == "__main__":
    main()

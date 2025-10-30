from python.pikahttp import Session


def main():
    session = Session()
    headers = {"User-Agent": "pikahttp/0.1.0"}
    response = session.request("GET", "https://api.github.com/zen", headers=headers)
    print(f"Status code: {response['status_code']}")
    print(f"Content: {response['content']}")


if __name__ == "__main__":
    main()

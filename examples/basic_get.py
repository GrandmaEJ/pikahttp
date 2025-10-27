from pikahttp import Session

def main():
    # Create a session
    session = Session()
    
    # Set headers
    headers = {
        "User-Agent": "pikahttp/0.1.0"
    }
    
    # Make GET request
    response = session.request("GET", "https://api.github.com/zen", headers=headers)
    
    # Print response
    print(f"Status code: {response['status_code']}")
    print(f"Content: {response['content'].decode()}")

if __name__ == "__main__":
    main()
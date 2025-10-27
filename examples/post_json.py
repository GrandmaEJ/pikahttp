from pikahttp import Session
import json

def main():
    # Create a session
    session = Session()
    
    # Set headers and data
    headers = {
        "User-Agent": "pikahttp/0.1.0",
        "Content-Type": "application/json"
    }
    
    data = {
        "title": "Test Post",
        "body": "This is a test post using pikahttp"
    }
    
    # Make POST request
    response = session.request(
        "POST", 
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers,
        body=json.dumps(data)
    )
    
    # Print response
    print(f"Status code: {response['status_code']}")
    print(f"Response data: {json.loads(response['content'])}")

if __name__ == "__main__":
    main()
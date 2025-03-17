import requests  # Importing the requests library for API communication

# Define API Base URL (Example API - JSONPlaceholder)
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# API Key (For demonstration, replace with actual API key if needed)
API_KEY = "your_api_key_here"

# Common Headers for Authentication (if required)
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",  # API key authentication
    "Content-Type": "application/json"  # Inform the server that we are sending JSON data
}

                # ======================== GET Request ========================

def fetch_posts():
    """Fetch all posts from the API."""
    try:
        response = requests.get(BASE_URL, headers=HEADERS)  # Sending a GET request
        response.raise_for_status()  # Raise an error if the response is unsuccessful (4xx, 5xx)

        posts = response.json()  # Convert JSON response to Python object (list)
        print("\n✅ Successfully fetched posts. Displaying first 3 posts:\n")
        
        for post in posts[:3]:  # Print only first 3 posts
            print(f"📌 ID: {post['id']}, Title: {post['title']}")
    
    except requests.exceptions.RequestException as e:
        print("\n❌ Error fetching posts:", e)  # Handle errors (network issue, bad response, etc.)



                   # ======================== POST Request ========================

def create_post(title, body, user_id):
    """Create a new post using the API."""
    post_data = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    try:
        response = requests.post(BASE_URL, json=post_data, headers=HEADERS)  # Sending a POST request
        response.raise_for_status()  # Raise an error if the request fails
        
        new_post = response.json()  # Convert JSON response to Python object
        print("\n✅ Post Created Successfully:")
        print(new_post)
    
    except requests.exceptions.RequestException as e:
        print("\n❌ Error creating post:", e)  # Handle errors


            # ======================== API Request with Authentication ========================
            
def fetch_protected_data():
    """Fetch protected data requiring authentication."""
    protected_url = "https://api.example.com/protected-endpoint"  # Replace with actual API endpoint

    try:
        response = requests.get(protected_url, headers=HEADERS)  # Authenticated request
        response.raise_for_status()  # Raise an error if authentication fails

        print("\n✅ Protected Data Retrieved Successfully:")
        print(response.json())  # Display data
    
    except requests.exceptions.RequestException as e:
        print("\n❌ Authentication Failed:", e)  # Handle authentication errors


            # ======================== Running the Functions ========================
            
if __name__ == "__main__":
    fetch_posts()  # Fetching posts from API
    create_post("Learn API Integration", "This is a test post created using Python.", 101)  # Creating a post
    fetch_protected_data()  # Fetching protected data (if API key is valid)

"""
Simple API Demo
This script demonstrates how to fetch a random quote from the API
without the web interface. Great for understanding the basics!
"""

import requests

def fetch_random_quote():
    """
    Fetch a random quote from the Kanye REST API.
    """
    try:
        print("Fetching quote from API...")
        response = requests.get('https://api.kanye.rest/', timeout=5)
        response.raise_for_status()
        
        quote_data = response.json()
        return {
            'content': quote_data.get('quote'),
            'author': 'Kanye West'
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    print("=" * 50)
    print("Quote API Demo")
    print("=" * 50)
    print()
    
    quote = fetch_random_quote()
    
    if quote:
        print(f"Quote: \"{quote['content']}\"")
        print(f"Author: {quote['author']}")
    else:
        print("Failed to fetch quote. Using fallback:")
        print("Quote: \"The only way to do great work is to love what you do.\"")
        print("Author: Steve Jobs")
    
    print()
    print("=" * 50)

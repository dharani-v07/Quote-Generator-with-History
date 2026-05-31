"""
Quote Generator with History
A beginner-friendly application that fetches random quotes from an API
and saves them to a database for history tracking.
"""

from flask import Flask, render_template, request
import sqlite3
import requests
import datetime
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)

# Database setup
DB_NAME = "quotes_history.db"

def get_db_connection():
    """
    Create a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def init_database():
    """
    Initialize the database table if it doesn't exist.
    This creates a table to store quote history.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            author TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def fetch_random_quote():
    """
    Fetch a random quote from the Kanye REST API.
    Returns a dictionary with quote content and author.
    If the API fails, returns a default quote.
    """
    try:
        # Using the Kanye REST API (very reliable and free)
        response = requests.get('https://api.kanye.rest/', timeout=5)
        response.raise_for_status()  # Raise an error for bad status codes
        
        quote_data = response.json()
        return {
            'content': quote_data.get('quote', 'No content available'),
            'author': 'Kanye West'
        }
    except Exception as e:
        print(f"Error fetching quote: {e}")
        # Return a fallback quote if API fails
        return {
            'content': 'The only way to do great work is to love what you do.',
            'author': 'Steve Jobs'
        }

def save_quote_to_db(content, author):
    """
    Save a quote to the database.
    
    Args:
        content (str): The quote text
        author (str): The quote author
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the quote into the database
    cursor.execute(
        'INSERT INTO quotes (content, author, timestamp) VALUES (?, ?, ?)',
        (content, author, datetime.datetime.now())
    )
    
    conn.commit()
    conn.close()

def get_quote_history(limit=10):
    """
    Retrieve the most recent quotes from the database.
    
    Args:
        limit (int): Maximum number of quotes to retrieve
    
    Returns:
        list: List of quote dictionaries
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get the most recent quotes
    cursor.execute(
        'SELECT content, author, timestamp FROM quotes ORDER BY timestamp DESC LIMIT ?',
        (limit,)
    )
    
    quotes = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    return [dict(quote) for quote in quotes]

# Routes

@app.route('/')
def index():
    """
    Home page - displays the current quote and quote history.
    """
    # Get current quote from session or fetch a new one
    current_quote = request.args.get('quote')
    current_author = request.args.get('author')
    
    if not current_quote:
        # No quote provided, show a welcome message
        current_quote = "Click 'Get New Quote' to start!"
        current_author = ""
    
    # Get quote history
    history = get_quote_history()
    
    return render_template(
        'index.html',
        current_quote=current_quote,
        current_author=current_author,
        history=history
    )

@app.route('/new-quote')
def new_quote():
    """
    Fetch a new random quote and save it to the database.
    """
    # Fetch a new quote from the API
    quote = fetch_random_quote()
    
    # Save to database
    save_quote_to_db(quote['content'], quote['author'])
    
    # Redirect to home page with the new quote
    return render_template(
        'index.html',
        current_quote=quote['content'],
        current_author=quote['author'],
        history=get_quote_history()
    )

@app.route('/history')
def history():
    """
    Display only the quote history page.
    """
    history = get_quote_history(limit=50)  # Show more quotes on history page
    return render_template('history.html', history=history)

@app.route('/clear-history')
def clear_history():
    """
    Clear all quotes from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM quotes')
    conn.commit()
    conn.close()
    
    return render_template(
        'index.html',
        current_quote="History cleared! Click 'Get New Quote' to start fresh.",
        current_author="",
        history=[]
    )

# Initialize the database when the app starts
init_database()

if __name__ == '__main__':
    print("Starting Quote Generator with History...")
    print("Open your browser and visit: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)

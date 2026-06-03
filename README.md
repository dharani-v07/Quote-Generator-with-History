# Quote Generator with History 🎯

A beginner-friendly web application that fetches random quotes from an external API and saves them to a database for history tracking. This project teaches API integration, database operations, and web development basics.

## Features ✨

- **Fetch Random Quotes**: Get inspiring quotes from the free Quotable API
- **Quote History**: Automatically saves every quote to a SQLite database
- **Beautiful UI**: Clean, modern interface with gradient design
- **View History**: Browse all your saved quotes with timestamps
- **Clear History**: Option to reset your quote history

## What You'll Learn 📚

- How to integrate with external APIs using Python
- Working with SQLite databases
- Building web applications with Flask
- Creating HTML templates with CSS styling
- Error handling and fallback mechanisms

## Prerequisites 📋

- Python 3.7 or higher installed on your computer
- Basic understanding of Python (variables, functions, loops)
- Internet connection (to fetch quotes from the API)

## Installation Steps 🚀

### Step 1: Install Python (if not already installed)

Download and install Python from [python.org](https://www.python.org/downloads/). During installation, make sure to check "Add Python to PATH".

### Step 2: Navigate to the Project Directory

Open your terminal or command prompt and navigate to the project folder:

```bash
cd "d:\VirtualWorksIntern\Quote Generator with History"
```

### Step 3: Create a Virtual Environment (Recommended)

A virtual environment keeps your project dependencies isolated:

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

You'll know it's activated when you see `(venv)` at the start of your command prompt.

### Step 5: Install Required Packages

Install Flask and requests library:

```bash
pip install -r requirements.txt
```

## Running the Application 🎮

Once you've completed the installation, run the application:

```bash
python app.py
```

You should see:
```
Starting Quote Generator with History...
Open your browser and visit: http://127.0.0.1:5000
```

### Open in Browser

Open your web browser and visit: **http://127.0.0.1:5000**

## How to Use 🎯

1. **Get a New Quote**: Click the "Get New Quote" button to fetch a random quote from the API
2. **View History**: See your recently saved quotes on the main page
3. **Full History**: Click "View Full History" to see all saved quotes
4. **Clear History**: Remove all saved quotes and start fresh

## Project Structure 📁

```
Quote Generator with History/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── index.html        # Main page with quote display
│   └── history.html      # Full history page
└── quotes_history.db     # SQLite database (created automatically)
```

## Code Explanation 📖

### Key Components

1. **API Integration** (`fetch_random_quote()` function):
   - Uses the `requests` library to call the Quotable API
   - Handles errors gracefully with a fallback quote
   - Returns quote content and author

2. **Database Operations**:
   - `init_database()`: Creates the SQLite table if it doesn't exist
   - `save_quote_to_db()`: Saves quotes with timestamps
   - `get_quote_history()`: Retrieves saved quotes

3. **Flask Routes**:
   - `/`: Home page displaying current quote and recent history
   - `/new-quote`: Fetches and saves a new quote
   - `/history`: Shows full quote history
   - `/clear-history`: Deletes all saved quotes

4. **HTML Templates**:
   - Clean, responsive design with CSS
   - Displays quotes in a card format
   - Shows history with timestamps

## Understanding the Code 💡

### API Call
```python
response = requests.get('https://api.quotable.io/random')
quote_data = response.json()
```
This sends a GET request to the API and parses the JSON response.

### Database Insert
```python
cursor.execute(
    'INSERT INTO quotes (content, author, timestamp) VALUES (?, ?, ?)',
    (content, author, datetime.datetime.now())
)
```
Uses parameterized queries to safely insert data into SQLite.

### Flask Route
```python
@app.route('/new-quote')
def new_quote():
    quote = fetch_random_quote()
    save_quote_to_db(quote['content'], quote['author'])
    return render_template('index.html', ...)
```
Defines a URL endpoint that fetches and saves a quote, then renders the template.

## Troubleshooting 🔧

### "Module not found" error
Make sure you've installed the requirements:
```bash
pip install -r requirements.txt
```

### API connection error
The app includes a fallback quote if the API is unavailable. Check your internet connection.

### Port already in use
If port 5000 is busy, change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

## Next Steps 🚀

Try modifying the code to learn more:

1. **Add more features**: Like copying quotes to clipboard
2. **Filter by author**: Add search functionality
3. **Export history**: Download quotes as a CSV file
4. **Add categories**: Fetch quotes from specific topics
5. **Add authentication**: Save quotes per user

## Resources 📚

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Library](https://requests.readthedocs.io/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Quotable API](https://github.com/lukePeavy/quotable)

## License 📄

This project is open source and available for educational purposes.

---

# CaptionCraft AI

CaptionCraft AI is a full-stack AI-powered marketing content generator designed for small businesses. The app helps users quickly create social media captions, hashtags, calls to action, and future content ideas based on their business type, platform, topic, tone, and target audience.

## Overview

Many small businesses need to post consistently on social media but may struggle with writing captions or coming up with content ideas. CaptionCraft AI solves this by turning simple user inputs into ready-to-use marketing content.

The app uses a frontend form to collect details from the user, sends that information to a Flask backend, and then uses the Gemini API to generate structured marketing content.

## Features

* Generates two caption options
* Creates relevant hashtags
* Suggests a call to action
* Provides a future content idea
* Allows users to choose business type, platform, tone, topic, and target audience
* Uses a Flask backend to handle AI requests
* Keeps the API key secure using an environment variable
* Can run locally on one computer
* Can also be tested across devices on the same local network

## Tech Stack

* HTML
* JavaScript
* Tailwind CSS
* Python
* Flask
* Gemini API
* python-dotenv

## How It Works

1. The user fills out the form on the webpage.
2. The frontend sends the user input to the Flask backend.
3. The backend creates a prompt using the form data.
4. The backend sends the prompt to the Gemini API.
5. Gemini returns generated marketing content.
6. The backend sends the response back as JSON.
7. The frontend displays the captions, hashtags, call to action, and future idea in separate cards.

## Project Structure

```text
CaptionCraftAI
├── index.html
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `.env` file is not included in this repository because it contains the private Gemini API key.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/RadicalRis/CaptionCraftAI.git
```

### 2. Navigate into the project folder

```bash
cd CaptionCraftAI
```

### 3. Create a virtual environment

```bash
py -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

Create a file called `.env` in the main project folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### 7. Run the Flask server

```bash
python server.py
```

### 8. Open the app

In your browser, go to:

```text
http://127.0.0.1:5050/
```

## Local Network Testing

The app can also be accessed by another device on the same local network.

In `server.py`, the Flask app can be run with:

```python
app.run(host="0.0.0.0", debug=True, port=5050, use_reloader=False)
```

Then another device on the same network can open:

```text
http://YOUR-COMPUTER-IP:5050/
```

For example:

```text
http://192.168.1.25:5050/
```

This only works when the main computer is turned on, the Flask server is running, and both devices are connected to the same network.

## Security Note

The `.env` file is intentionally not uploaded to GitHub because it contains the private Gemini API key. The `.gitignore` file prevents sensitive or unnecessary files from being committed, including:

```text
.env
venv/
__pycache__/
*.pyc
.DS_Store
```

This keeps the API key private and avoids uploading large virtual environment files.

## What I Learned

Through this project, I learned how to build a full-stack web application with a frontend and backend. I also learned how to connect a Python Flask server to an AI API, handle JSON responses, protect API keys using environment variables, and test a local web app across devices on the same network.

This project helped me better understand how real web applications are structured, especially how the frontend, backend, and external APIs work together.

## Future Improvements

Possible future upgrades include:

* Add copy buttons for generated captions and hashtags
* Add a content history feature using local storage
* Add user accounts
* Add more platform-specific formatting
* Improve error messages on the page
* Deploy the app online using a production server
* Add screenshots or a demo video to the README

## Author

Created by [RadicalRis](https://github.com/RadicalRis).

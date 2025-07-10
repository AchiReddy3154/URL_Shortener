# URL Shortener

A simple, modern, and production-ready URL shortener built with Flask.

## Features

- Shorten long URLs to easy-to-share links
- View usage statistics and analytics for each short URL
- Minimal, clean, and user-friendly interface
- No authentication required—public and ready to use
- Ready for deployment on platforms like Render, Heroku, or your own server
## Screenshots

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9dcfcb68-cbd3-4861-9650-4c60d8d00e79" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/853b4630-a7fc-4b17-9888-9fa3cf4f2b0c" />


## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/AchiReddy3154/URL_Shortener.git
   cd URL_Shortener/url_shortener
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate  # On Mac/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Copy the example environment file and edit as needed:
   ```
   copy .env.example .env   # On Windows
   cp .env.example .env     # On Mac/Linux
   ```

### Running Locally

```
flask run
```

The app will be available at `http://localhost:5000`.

### Deployment

- The project includes `gunicorn.conf.py` and `render.yaml` for easy deployment to Render or similar platforms.
- Make sure to set your environment variables in production.

## Project Structure

```
url_shortener/
├── app.py
├── requirements.txt
├── gunicorn.conf.py
├── render.yaml
├── .env.example
├── templates/
│   ├── index.html
│   ├── stats.html
│   ├── error.html
│   ├── password.html
│   └── analytics.html
└── static/
```

## License

This project is open source and available under the MIT License.

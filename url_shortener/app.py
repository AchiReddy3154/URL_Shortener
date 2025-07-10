from flask import Flask, request, jsonify, render_template, redirect, abort, url_for
from pymongo import MongoClient
import random
import string
import datetime
import qrcode
import io
import base64
from bson import ObjectId
import bcrypt  # Still used for password-protected links, not user auth
import validators
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import pandas as pd
from urllib.parse import urlparse
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')

# MongoDB connection (robust, fallback to default if env not set)
MONGODB_URI = os.getenv('MONGODB_URI') or 'mongodb://localhost:27017/urlshortener'
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    db_name = MONGODB_URI.split('/')[-1].split('?')[0] or 'urlshortener'
    db = client[db_name]
    print(f"Connected to MongoDB: {db_name}")
except Exception as e:
    print(f"MongoDB connection failed: {e}\nCheck your MONGODB_URI and MongoDB server.")
    db = None

# Global stats dashboard route
@app.route('/stats')
def stats_dashboard():
    # Aggregate all URLs
    urls = list(db.urls.find({}))
    urls_created = len(urls)
    total_clicks = sum(url.get('clicks', 0) for url in urls)
    now = datetime.datetime.utcnow()

    # Prepare URLs for table and fix date fields for display
    for url in urls:
        # Convert MongoDB datetime to Python datetime if needed
        if not isinstance(url.get('created_at'), datetime.datetime):
            try:
                url['created_at'] = datetime.datetime.strptime(str(url['created_at']), '%Y-%m-%d %H:%M UTC')
            except Exception:
                url['created_at'] = None
        if url.get('expires_at') and not isinstance(url.get('expires_at'), datetime.datetime):
            try:
                url['expires_at'] = datetime.datetime.strptime(str(url['expires_at']), '%Y-%m-%d %H:%M UTC')
            except Exception:
                url['expires_at'] = None
        # Defensive: ensure clicks is int
        url['clicks'] = int(url.get('clicks', 0))
        # Defensive: ensure long_url is str
        url['long_url'] = str(url.get('long_url', ''))
        # Defensive: ensure short_code is str
        url['short_code'] = str(url.get('short_code', ''))

    # Clicks chart (all URLs combined)
    click_times = []
    for url in urls:
        # Defensive: click_times may be list of datetimes or strings
        for ct in url.get('click_times', []):
            if isinstance(ct, datetime.datetime):
                click_times.append(ct)
            else:
                try:
                    click_times.append(datetime.datetime.fromisoformat(str(ct)))
                except Exception:
                    pass
    clicks_chart = None
    if click_times:
        df = pd.DataFrame({'timestamp': click_times})
        df['date'] = df['timestamp'].dt.date
        daily_clicks = df.groupby('date').size().reset_index(name='clicks')
        fig = px.line(daily_clicks, x='date', y='clicks', title='Click Activity', labels={'date': 'Date', 'clicks': 'Number of Clicks'})
        clicks_chart = fig.to_html(full_html=False)

    # Show all available features in the dashboard context
    features = [
        "Shorten URLs with custom codes",
        "Password-protected links (PIN)",
        "Expiration dates for links",
        "Scheduled activation/expiration",
        "QR code generation",
        "Click analytics and charts",
        "Global stats dashboard",
        "No authentication required",
        "Mobile/LAN/public access",
        "Malicious URL protection"
    ]
    return render_template(
        'stats.html',
        urls=urls,
        urls_created=urls_created,
        total_clicks=total_clicks,
        clicks_chart=clicks_chart,
        now=now,
        features=features,
        show_global_stats=True
    )

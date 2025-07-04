import os
import requests
from flask import Flask, request, redirect, session, render_template, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_URL = 'https://api.spotify.com/v1'

SCOPE = 'user-top-read'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    auth_url = f"{SPOTIFY_AUTH_URL}?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    response = requests.post(SPOTIFY_TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    response_data = response.json()
    session['access_token'] = response_data.get('access_token')
    return redirect(url_for('stats'))

@app.route('/stats')
def stats():
    access_token = session.get('access_token')
    if not access_token:
        return redirect(url_for('login'))
    
    headers = {"Authorization": f"Bearer {access_token}"}

    # Poprawne pobranie top artysty
    top_artists = requests.get(f"{SPOTIFY_API_URL}/me/top/artists?limit=1", headers=headers).json()
    top_artist = None
    if top_artists.get('items'):
        top_artist = top_artists['items'][0]

    # Top 5 utworów
    top_tracks = requests.get(f"{SPOTIFY_API_URL}/me/top/tracks?limit=5", headers=headers).json()

    total_ms = sum(track['duration_ms'] for track in top_tracks['items'])
    total_minutes = total_ms / 1000
    
    return render_template(
        'stats.html',
        top_artist=top_artist,
        top_tracks=top_tracks['items'],
        total_minutes=round(total_minutes, 2)
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
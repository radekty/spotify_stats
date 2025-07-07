# 🎵 Spotify Stats

**Spotify Stats** is a simple web app built with **Python + Flask** that lets you:

- Log in with your Spotify account (OAuth)
- See your Top Tracks and Top Artists for different time ranges
- View your Recently Played tracks
- Sort your top tracks by popularity
- Control the number of displayed tracks with a slider (3–50)
- Instantly create a playlist on your Spotify account based on the tracks you see!

---

## 🚀 **Tech Stack**

- Python 3.x
- Flask
- Jinja2 templates
- Requests library
- Spotify Web API
- `.env` file for storing secrets securely

---

## ✅ **How to run it locally**

1️⃣ **Clone the repository**

```bash
git clone https://github.com/radekty/spotify-stats.git
cd spotify-stats
```

2️⃣ Create & activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Create a .env file

In the root folder, create a file named .env and add your Spotify credentials:
```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://127.0.0.1:5000/callback
```

🔒 Never commit .env to your repository!
Make sure .env is listed in your .gitignore.

5️⃣ Run the app

```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser.

📌 How to set up Spotify API
```
1.Go to Spotify Developer Dashboard.
2.Create an app.
3.Add the Redirect URI: http://127.0.0.1:5000/callback
4.Copy the Client ID and Client Secret and put them in your .env.
```

✨ Features
```
✅ Spotify OAuth login
✅ View Top Tracks & Top Artists
✅ Select time ranges: All Time, Last Year, Last Month
✅ See Recently Played
✅ Sort tracks by popularity
✅ Slider to choose number of tracks (3–50)
✅ Create playlist based on the current view
✅ Spotify-inspired UI (dark theme, green accents)
```

🗂️ Project Structure
```
spotify_stats/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── stats.html
├── static/
│   └── css/
│       └── style.css
├── .env
├── requirements.txt
```

⚙️ Important
The app requires the following Spotify scopes:
```
user-top-read
user-read-recently-played
playlist-modify-public
playlist-modify-private
```

If you change scopes, you’ll need to log in again to refresh the token.

📜 License
This is an educational / personal project — use and adapt it as you like.


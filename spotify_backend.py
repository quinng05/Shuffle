from spotipy.oauth2 import SpotifyOAuth
import spotipy
import os

os.environ['SPOTIPY_CLIENT_ID'] = "e9ef8eb0201a437aae11405d1d7473c6"
os.environ['SPOTIPY_CLIENT_SECRET'] = "2f60995745644f01ba8771608a5af26b"
os.environ['SPOTIPY_REDIRECT_URI'] = "http://localhost:8080/callback"
os.environ['SPOTIPY_DEBUG'] = "true"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="e9ef8eb0201a437aae11405d1d7473c6",
    client_secret="2f60995745644f01ba8771608a5af26b",
    redirect_uri="http://localhost:8080/callback",
    scope="user-library-read playlist-read-private"
))

# Fetch playlists
def get_playlists():
    playlists = sp.current_user_playlists()
    playlist_names = []
    for playlist in playlists['items']:
        if playlist is None:
            print("Warning: Encountered None value in playlists['items']")
            continue
        playlist_names.append(playlist['name'])
    return playlist_names

if __name__ == "__main__":
    print("Fetching Playlists...")
    print(get_playlists())


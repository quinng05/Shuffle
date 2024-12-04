from spotipy.oauth2 import SpotifyOAuth
import spotipy

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="http://localhost:8888/callback",
    scope="user-library-read playlist-read-private"
))

# Fetch playlists
def get_playlists():
    playlists = sp.current_user_playlists()
    return [playlist['name'] for playlist in playlists['items']]

if __name__ == "__main__":
    print("Fetching Playlists...")
    print(get_playlists())

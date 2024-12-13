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

# Get all songs
def sort_all_songs():
    playlists = sp.current_user_playlists()
    all_tracks = []

    # Iterate through each playlist
    for playlist in playlists['items']:
        if playlist is None:
            continue

        # Fetch tracks for the playlist
        tracks = sp.playlist_items(playlist['id'])
        for track in tracks['items']:
            track_info = track.get('track')
            if track_info:  # Avoid NoneType for track
                # Collect relevant information
                all_tracks.append({
                    'name': track_info['name'],
                    'popularity': track_info['popularity'],
                    'artists': ', '.join(artist['name'] for artist in track_info['artists']),
                    'album': track_info['album']['name']
                })

    # Sort tracks by popularity in descending order
    sorted_tracks = sorted(all_tracks, key=lambda x: x['popularity'], reverse=True)

    # Print sorted tracks
    for track in sorted_tracks:
        print(
            f"Name: {track['name']}, Popularity: {track['popularity']}, Artists: {track['artists']}, Album: {track['album']}")

    return sorted_tracks



# Fetch playlists
def get_playlists():
    playlists = sp.current_user_playlists()
    playlist_names = []
    for playlist in playlists['items']:
        if playlist is None:
            print("Warning: Encountered None value in playlists['items']")
            continue

        # Fetch tracks for the playlist
        tracks = sp.playlist_items(playlist['id'])
        for track in tracks['items']:
            track_info = track.get('track')
            if track_info:  # Avoid NoneType for track
                print("  ", track_info['name'], track_info['popularity'])
    return playlist_names

if __name__ == "__main__":
    print("Fetching Playlists...")
    print(get_playlists())
    print("Sorting All Songs by Popularity...")
    sorted_tracks = sort_all_songs()


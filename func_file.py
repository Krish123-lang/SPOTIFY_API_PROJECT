"""
This Python script utilizes the Spotipy library and the Spotify Web API to retrieve various details about albums, tracks, artists, and playlists from Spotify. It asks the user for input to specify the type of information they want to retrieve.

This Python script also showcases utilization of LyricsGenius library to retrieve lyrics for a given track.
 
"""

# Importing necessary libraries and setting up authentication using Spotify client credentials

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
import lyricsgenius

client_id = "<YOUR_SPOTIFY_CLIENT_ID>"
client_secret = "<YOUR_SPOTIFY_CLIENT_SECRET>"

auth_url = 'https://accounts.spotify.com/api/token'
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(auth_url, data=auth_data)

data = response.json()
data_access = data["access_token"]

headers = {'Authorization': f'Bearer {data_access}'}

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

base_url = "https://api.spotify.com/v1/"
# --------------------------------------------------------------------------------------------------


def get_albums(user_input):
    if user_input == "albums":
        input_album_name = str(input("Enter album name (Example: Different World) : ")).lower()
        preferred_album_url = f"{base_url}search?q={input_album_name}&type=album"
        album_response = requests.get(preferred_album_url, headers=headers)
        album_json = album_response.json()

        artist_name = album_json["albums"]["items"][0]["artists"][0]["name"]
        artist_id = album_json["albums"]["items"][0]["artists"][0]["id"]
        artist_url = album_json["albums"]["items"][0]["artists"][0]["external_urls"]["spotify"]

        album_name = album_json["albums"]["items"][0]["name"]
        album_url = album_json["albums"]["items"][0]["external_urls"]["spotify"]
        album_id = album_json["albums"]["items"][0]["id"]

        album_release_date = album_json["albums"]["items"][0]["release_date"]

        album_image_url = album_json["albums"]["items"][0]["images"][0]["url"]
        total_tracks_in_this_album = album_json["albums"]["items"][0]["total_tracks"]

        with open(f"{album_name}_details.txt", "w") as album_file:
            album_file.write(f"""
            *** ALBUM DETAILS ***

The album {album_name} artist name: {artist_name}
The album {album_name} artist id: {artist_id}
The album {album_name} artist url: {artist_url}
The album {album_name} url: {album_url}
The album {album_name} id: {album_id}
The album {album_name} release date: {album_release_date}
The album {album_name} image url: {album_image_url}
The album {album_name} total tracks: {total_tracks_in_this_album}
            """)

        # GET ALBUMS TRACKS
        album_tracks = requests.get(f"https://api.spotify.com/v1/albums/{album_id}/tracks", headers=headers)
        track_json = album_tracks.json()

        i = 0
        with open(f"album_track_details.txt", "w") as album_track_file:
            while i < total_tracks_in_this_album:
                track_name = track_json["items"][i]["name"]
                track_id = track_json["items"][i]["id"]
                track_link = track_json["items"][i]["external_urls"]["spotify"]
                track_preview_url = track_json["items"][i]["preview_url"]

                album_track_file.write(f"*** {track_name} Details ***\n\n")

                album_track_file.write(f"The track name is: {track_name}\n")
                album_track_file.write(f"The track id is: {track_id}\n")
                album_track_file.write(f"The track link is: {track_link}\n")
                album_track_file.write(f"The track preview is available on: {track_preview_url}\n\n")

                i += 1


def get_tracks(user_input):
    if user_input == "tracks":
        input_track_name = str(input("Enter album name (Example: Despacito) : ")).lower()
        preferred_track_url = f"{base_url}search?q={input_track_name}&type=track"
        track_response = requests.get(preferred_track_url, headers=headers)
        track_json = track_response.json()

        track_url = track_json["tracks"]["items"][0]["external_urls"]["spotify"]
        track_id = track_json["tracks"]["items"][0]["id"]
        track_name = track_json["tracks"]["items"][0]["name"]
        track_popularity = track_json["tracks"]["items"][0]["popularity"]
        track_preview_url = track_json["tracks"]["items"][0]["preview_url"]
        track_artist_name = track_json["tracks"]["items"][0]["album"]["artists"][0]["name"]

        with open(f"{track_name}_details.txt", "w") as track_file:
            track_file.write(f"""

           *** {track_name} Details ***

The track name is: {track_name}
The track id is: {track_id}
The track URL is: {track_url}
The track's artist name is: {track_artist_name}
The track popularity is: {track_popularity}
The track preview is available on: {track_preview_url}
            """)
        token = "<YOUR_LYRICSGENIUS_ACCESS_TOKEN>"
        genius = lyricsgenius.Genius(token)

        song = genius.search_song(track_name, track_artist_name)

        with open(f"{track_name}_lyrics.txt", "w", encoding="utf-8") as lyrics_file:
            lyrics_file.write(song.lyrics)
            lyrics_file.close()


def get_artist(user_input):
    if user_input == "artists":
        input_artist_name = str(input("Enter artist name (Example: Imagine Dragons) : ")).lower()
        preferred_artist_url = f"{base_url}search?q={input_artist_name}&type=artist"
        artist_response = requests.get(preferred_artist_url, headers=headers)
        artist_json = artist_response.json()

        artist_name_s = artist_json["artists"]["items"][0]["name"]
        artist_id_number = artist_json["artists"]["items"][0]["id"]
        artist_image_url = artist_json["artists"]["items"][0]["images"][0]["url"]
        artist_url_page = artist_json["artists"]["items"][0]["external_urls"]["spotify"]
        artist_total_followers = artist_json["artists"]["items"][0]["followers"]["total"]
        artist_genres = artist_json["artists"]["items"][0]["genres"]
        artist_popularity = artist_json["artists"]["items"][0]["popularity"]

        with open(f"artist_details.txt", "w") as artist_file:
            artist_file.write(f"""

            *** {artist_name_s} Details ***

The artist name is: {artist_name_s}
The artist id is: {artist_id_number}
The artist image can be found on: {artist_image_url}
The artist URL is: {artist_url_page}
The artist total followers are: {artist_total_followers}
The artist genres are: {artist_genres}
The artist popularity is: {artist_popularity}
            """)


def get_playlist(user_input):
    if user_input == "playlists":
        input_playlist_name = str(input("Enter artist name (Example: RapCaviar) : ")).lower()
        preferred_playlist_url = f"{base_url}search?q={input_playlist_name}&type=playlist"
        playlist_response = requests.get(preferred_playlist_url, headers=headers)
        playlist_json = playlist_response.json()

        playlist_name = playlist_json["playlists"]["items"][0]["name"]
        playlist_id = playlist_json["playlists"]["items"][0]["id"]
        playlist_desc = playlist_json["playlists"]["items"][0]["description"]
        playlist_url = playlist_json["playlists"]["items"][0]["external_urls"]["spotify"]
        playlist_image = playlist_json["playlists"]["items"][0]["images"][0]["url"]
        playlist_total_tracks = playlist_json["playlists"]["items"][0]["tracks"]["total"]

        playlist_owner_name = playlist_json["playlists"]["items"][0]["owner"]["display_name"]
        playlist_owner_id = playlist_json["playlists"]["items"][0]["owner"]["id"]
        playlist_owner_url = playlist_json["playlists"]["items"][0]["owner"]["external_urls"]["spotify"]

        tracks_in_playlist = sp.user_playlist_tracks(playlist_owner_name, playlist_id)
        tracks = tracks_in_playlist["items"]

        while tracks_in_playlist["next"]:
            tracks_in_playlist = sp.next(tracks_in_playlist)
            tracks.extend(tracks_in_playlist["items"])

        with open(f"{playlist_name}.txt", "w") as playlist_file:
            playlist_file.write(f"""
            
        *** PLAYLIST DETAILS ***

Playlist's Name: {playlist_name}
Playlist's Id: {playlist_id}
Playlist's Description: {playlist_desc}
Playlist's URL: {playlist_url}
Playlist's Image: {playlist_image}
Playlist Total Tracks: {playlist_total_tracks}


        *** PLAYLIST OWNER DETAILS ***

Playlist's Owner Name: {playlist_owner_name}
Playlist's Owner Id: {playlist_owner_id}
Playlist's Owner URL: {playlist_owner_url}

            """)

            playlist_file.write(f"""
*** TRACKS IN THIS PLAYLIST ***
            """)

            for track in tracks:
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                album_name = track['track']['album']['name']

                playlist_file.write(f"""
Track name: {track_name}
Artist name: {artist_name}
Album name: {album_name}
                """)

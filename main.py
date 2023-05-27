"""
This Python Script is importing functions "get_albums", "get_tracks", "get_artist", and "get_playlist" from "func_file.py" file.
It prompts the user to enter a search term (either "Albums", "Tracks", "Artists", or "Playlists") and then calls the corresponding function based on the user's input.
"""

from func_file import get_albums, get_tracks, get_artist, get_playlist


# Ask user to enter a search term by calling input() function. Then the search term is converted to lowercase using the ".lower()" method.

user_input = str(input("Enter the term you want to search (Albums/Tracks/Artists/Playlists): ")).lower()


# If the user entered "albums", it calls the get_albums() function, which asks the user to enter an album name, retrieves album details from Spotify, and saves the album details and track details in text files.

get_albums(user_input)

# If the user entered "tracks", it calls the get_tracks() function, which asks the user to enter a track name, retrieves track details from Spotify, and saves the track details and lyrics in a text file.

get_tracks(user_input)

# If the user entered "artists", it calls the get_artist() function, which asks the user to enter an artist name, retrieves artist details from Spotify, and saves the artist details in a text file.

get_artist(user_input)

# If the user entered "playlists", it calls the get_playlist() function, which asks the user to enter a playlist name, retrieves playlist details and tracks from Spotify, and saves the playlist details and track details in a text file.

get_playlist(user_input)

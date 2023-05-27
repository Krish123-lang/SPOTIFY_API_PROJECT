# SPOTIFY API PROJECT

## About Spotify Web API
The Spotify Web API is an application programming interface (API) provided by Spotify that allows developers to interact with and access various resources and functionalities of the Spotify music streaming platform. It provides a set of endpoints and methods that enable developers to retrieve data about music tracks, albums, artists, playlists, user profiles, and more.
With the Spotify Web API, developers can integrate Spotify's music catalog and related features into their own applications, websites, or services. They can create music recommendation systems, build music player applications, analyze music data, curate playlists, and perform various operations related to music streaming and user interactions.

The API supports various functionalities, including:
1. Searching for music tracks, albums, artists, and playlists based on different criteria.
2. Accessing details about specific tracks, albums, artists, or playlists, such as metadata, images, popularity, release dates, and more.
3. Retrieving audio features of tracks, including tempo, danceability, energy, and more.
4. Managing and interacting with user playlists, such as creating, modifying, and adding or removing tracks.
5. Retrieving and updating user profiles, playlists, and their associated information.
6. Controlling playback of music on users' devices using Spotify Connect.
7. Accessing user-specific data, such as their saved tracks, recently played tracks, and top tracks or artists.

The Spotify Web API uses standard HTTP methods (GET, POST, PUT, DELETE) and returns responses in JSON format. To access the API, developers need to obtain authentication credentials (Client ID and Client Secret) and include them in their API requests. The API provides both public endpoints, which can be accessed without user authentication, and private endpoints that require user authorization to access user-related data.



## About The Project
This project utilizes the Spotipy library and the Spotify Web API to retrieve various details about albums, tracks, artists, and playlists from Spotify. It asks the user for input to specify the type of information they want to retrieve.
This project also showcases utilization of LyricsGenius library to retrieve lyrics for a given track.

1. It imports the necessary libraries and sets up authentication using Spotify client credentials.
2. The user is prompted to enter a category (albums, tracks, artists, or playlists) and the corresponding information is retrieved from the Spotify API.
3. For albums, it retrieves details such as the artist, release date, image URL, and total tracks. It then saves the album details in a text file named after "album_name" `_details.txt`.
4. It also retrieves the tracks within the album and saves their details in a separate text file named `album_track_details.txt`.
5. For tracks, it retrieves details such as the track URL, ID, popularity, preview URL, and artist name. It saves the track details in a text file named after "track_name" `_details.txt`.
6. It uses the LyricsGenius library to search for and retrieve the lyrics of the track. The lyrics are saved in a text file named after track_name `_lyrics.txt`.
7. For artists, it retrieves details such as the artist's name, ID, image URL, URL page, total followers, genres, and popularity. The artist details are saved in a text file named `artist_details.txt`.
8. For playlists, it retrieves details such as the playlist name, ID, description, URL, image, total tracks, playlist owner name, ID, and URL. The playlist details are saved in a text file named after "playlist_name" `.txt`. Additionally, it retrieves the tracks within the playlist and saves their details in the same text file.
9. The code uses the Spotipy library to handle paginated responses for playlists and retrieves all tracks in the playlist.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.

1. First of all create an developer account on [Spotify Developer](https://developer.spotify.com/). Then, create your new app. Then,  you will get the CLIENT_ID, CLIENT_SECRET and ACCESS TOKEN. Save it somewhere.
2. You also need to sign in to the [Lyrics Genius](https://genius.com/developers) to get the tracks lyrics. Then, click on [Create New API Client](https://genius.com/api-clients/new). Then, create a new app. Then, you will get CLIENT_ID, CLIENT_SECRET and CLIENT_ACCESS_TOKEN, save it somewhere. 
3. Then, create a isolated environment in your folder using following commands

```bash
i) virtualenv env
ii) source env/Scripts/activate

```

3. Then install tools using  

 ```python
 pip install -r requirements.txt
```

4. All of the packages needed in this project are installed 😀.
5. Then use `python3 main.py` to run the script.
6. You can also see the output that I have provided with this repository. (Note: The output files are in text file)

https://github.com/Krish123-lang/SPOTIFY_API_PROJECT/assets/56486342/0e0740c9-8c3b-4223-acf0-7d554c370dd9

Thank You. 🙏

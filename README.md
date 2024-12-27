# Music Management System
### Developed by JOHN GAITHO (Music Producer & Developer).

This is a Music Management System, a command-line interface (CLI) application designed to manage artists, albums, and tracks in a music database. It uses SQLAlchemy for database operations and SQLite as the database engine. The application allows you to create, delete, and view artists, albums, and tracks.
An artist can have multiple albums (one-to-many relationship), meaning one artist can release many albums. Each album can contain multiple tracks (one-to-many relationship), so an album can have many songs or pieces of music. Each track is associated with exactly one album (many-to-one relationship). This ensures that artists are connected to their albums.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
- [License](#license)

## Features
- **Artist Management**: Create, delete, list, and find artists by ID.
- **Album Management**: Create, delete, list, and find albums by ID.
- **Track Management**: Create, delete, list, and find tracks by ID.
- **SQLite Database**: Stores all data in a lightweight SQLite database (`music.db`).

## Technologies Used
- **Python 3**: The main programming language used to implement the system.
- **SQLAlchemy**: ORM used for interacting with the SQLite database.
- **SQLite**: A lightweight database engine used to store data.
- **Click**: A Python library used to create the command-line interface (CLI) for this application.

## Requirements
- **Python 3.x**: This application is built using Python 3.8+.
- **SQLAlchemy**: ORM used for handling the database.
- **Click**: Used for managing the command-line interface.

### Install Dependencies

Before running the application, you need to install the required dependencies:

1. **Clone the repository**:
   - First, clone the repository to your local machine using Git.

   ```bash
   git clone https://github.com/John-Gaitho/Music-Management-System.git
   
   cd Music-Management-System
   ```
###  Install this in the terminal for dependencies.
   ```bash
   pipenv install
   pipenv shell

   pip install click
  ```
### Add this code into the pipfile;
   ```bash
  click = "*"
sqlalchemy = "*"
```


###   How to Run
To run the Music Management System, use the following command:
bash
Copy code
```bash
python cli.py
```
This will display the available commands in the terminal, and you can execute the relevant commands as per your requirements.
### How to Use
The Music Management System offers commands to manage artists, albums, and tracks. Below are examples of how to use each feature:
Artist Management
Create an Artist:
To create a new artist, use the following command with the artist's name:
Copy code
```bash
python cli.py create-artist-cli <artist_name>
```
Example:
Copy code
```bash
python cli.py create-artist-cli "John swaga"
```

To delete an artist by ID:
bash
Copy code
```bash
python cli.py delete-artist-cli <artist_id>
```
Copy code
python cli.py list-artists

To find an artist by their ID:
bash
Copy code
```bash
python cli.py find-artist <artist_id>
```

To create an album for a specific artist, use the following command with the album title and artist ID:

```bash
python cli.py create-album-cli <album_title> <artist_id>
```
Example:
bash
Copy code
```bash
python cli.py create-album-cli "christmas night" 1
```

To delete an album by ID:
bash
Copy code
```bash
python cli.py delete-album-cli <album_id>
```
Example:

```bash
python cli.py delete-album-cli 1
```

To list all albums in the system:

Copy code
```bash
python cli.py list-albums
```

To find an album by its ID:

Copy code
```bash
python cli.py find-album <album_id>
```

To create a track for a specific album, use the following command with the track title and album ID:

Copy code
```bash
python cli.py create-track-cli <track_title> <album_id>
```
Example:
bash
Copy code
```bash
python cli.py create-track "Track 1" 1
```
To delete a track by ID:
bash
Copy code
```bash
python cli.py delete-track-cli <track_id>
```
Example:
bash
Copy code
```bash
python cli.py delete-track-cli 1
```
To list all tracks in the system:
bash
Copy code
```bash
python cli.py list-tracks
```
To find a track by its ID:
bash
Copy code
```bash
python cli.py find-track <track_id>
```

### Support and Contact Details
Incase of any query, need for collaboration or issues with this code, feel free to reach me at jgaitho@gmail.com

License
MIT License

Copyright © 2024 John-Gaitho

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




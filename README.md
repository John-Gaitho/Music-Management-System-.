# Music Management System

This Music Management System is a command-line interface (CLI) application designed to manage artists, albums, and tracks in a music database. It uses SQLAlchemy for database operations and SQLite as the database engine. The application allows you to create, delete, and view artists, albums, and tracks.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [How to Use](#how-to-use)
  - [Artist Management](#artist-management)
  - [Album Management](#album-management)
  - [Track Management](#track-management)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Artist Management**: Create, delete, list, and find artists by ID.
- **Album Management**: Create, delete, list, and find albums by ID.
- **Track Management**: Create, delete, list, and find tracks by ID.
- **SQLite Database**: Stores all data in a lightweight SQLite database (`music.db`).

## Technologies Used
- **Python 3.x**: The main programming language used to implement the system.
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
python cli.py create-artist <artist_name>
```
Example:

Copy code
```bash
python cli.py create-artist-cli "John Doe"
```
Delete an Artist:
To delete an artist by ID:

bash
Copy code
```bash
python cli.py delete-artist-cli <artist_id>
```
Copy code
python cli.py list-artists
Find an Artist by ID:
To find an artist by their ID:

bash
Copy code
python cli.py find-artist <artist_id>
Example:

bash
Copy code
python cli.py find-artist 1
Album Management
Create an Album:
To create an album for a specific artist, use the following command with the album title and artist ID:

bash
Copy code
python cli.py create-album <album_title> <artist_id>
Example:

bash
Copy code
python cli.py create-album "Greatest Hits" 1
Delete an Album:
To delete an album by ID:

bash
Copy code
python cli.py delete-album <album_id>
Example:

bash
Copy code
python cli.py delete-album 1
List all Albums:
To list all albums in the system:

bash
Copy code
python cli.py list-albums
Find an Album by ID:
To find an album by its ID:

bash
Copy code
python cli.py find-album <album_id>
Track Management
Create a Track:
To create a track for a specific album, use the following command with the track title and album ID:

bash
Copy code
python cli.py create-track <track_title> <album_id>
Example:

bash
Copy code
python cli.py create-track "Track 1" 1
Delete a Track:
To delete a track by ID:

bash
Copy code
python cli.py delete-track <track_id>
Example:

bash
Copy code
python cli.py delete-track 1
List all Tracks:
To list all tracks in the system:

bash
Copy code
python cli.py list-tracks
Find a Track by ID:
To find a track by its ID:

bash
Copy code
python cli.py find-track <track_id>

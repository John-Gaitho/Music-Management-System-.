# Music Management System

The Music Management System is a command-line interface (CLI) application designed to manage artists, albums, and tracks in a music database. It uses SQLAlchemy for database operations and SQLite as the database engine. The application allows you to create, delete, and view artists, albums, and tracks.

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

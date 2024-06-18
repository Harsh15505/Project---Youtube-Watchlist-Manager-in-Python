# YouTube Watchlist Manager

Drowning in YouTube's "Watch Later" list? Tame the queue with this manager—add, track, and watch at your own pace!

## Features

- **Add videos to your watchlist**: Easily add YouTube videos to your personalized watchlist.
- **List all videos in your watchlist**: View all the videos in your watchlist along with relevant details.
- **Remove videos from your watchlist**: Remove videos from your watchlist when you're done watching or no longer interested.
- **Calculate the total estimated watch time**: Know the total time required to watch all the videos in your list.
- **Automatic removal of unwatched videos**: Set a time limit for how long videos can stay in your watchlist before being automatically removed.

## Getting Started

### Prerequisites

- Python 3.x
- YouTube Data API key

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/youtube-watchlist-manager.git
    cd youtube-watchlist-manager
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the project root directory and add your YouTube Data API key:

    ```plaintext
    Google_API_key=YOUR_API_KEY_HERE
    ```

### Usage

1. **Run the script**:

    ```bash
    python '.\Project - Youtube Watch List.py'
    ```

2. **Follow the on-screen instructions** to manage your YouTube watchlist:

    - **List all videos**: Displays all videos currently in your watchlist.
    - **Add a video**: Prompts you to enter a YouTube video link to add it to your watchlist.
    - **Remove a video**: Allows you to remove a video by its index in the list.
    - **Calculate total watch time**: Displays the total estimated watch time for all videos in the watchlist.
    - **Change date limit**: Modify the time limit for automatic removal of unwatched videos.

### Configuration

- **Date limit for automatic removal**: You can change the time limit (in days) for how long videos remain in your watchlist by selecting the appropriate option in the menu.



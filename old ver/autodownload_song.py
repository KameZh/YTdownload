import os
import yt_dlp
import pygame

def get_audio_stream(song_name):
    """
    Fetch the audio stream URL for a given song name using yt-dlp.
    :param song_name: The name of the song to search for
    :return: Audio stream file path or None if not found
    """
    search_url = f"ytsearch:{song_name}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'outtmpl': 'temp_song.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_url, download=True)
        return ydl.prepare_filename(info)

def play_audio(file_path):
    """
    Play the downloaded audio using pygame.
    :param file_path: Path to the audio file
    """
    print("Initializing player...")
    pygame.init()
    pygame.mixer.init()

    try:
        print(f"Playing: {file_path}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Wait while the music plays

    except Exception as e:
        print(f"Error playing audio: {e}")
    finally:
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

def main():
    song_name = input("Enter the name of the song you want to play: ")
    print("Searching for the song...")
    file_path = get_audio_stream(song_name)
    
    if file_path and os.path.exists(file_path):
        print("Song downloaded successfully! Playing now...")
        play_audio(file_path)
    else:
        print("Sorry, couldn't find or play the song.")

if __name__ == "__main__":
    main()

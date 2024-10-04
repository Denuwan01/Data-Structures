class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

class PlaylistManager:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = self.tail = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song

    def play_next(self, current_song):
        if not current_song or not current_song.next:
            print("No next song to play.")
            return None
        next_song = current_song.next
        print(f"Playing next song: {next_song.title} by {next_song.artist}")
        return next_song

    def play_prev(self, current_song):
        if not current_song or not current_song.prev:
            print("No previous song to play.")
            return None
        prev_song = current_song.prev
        print(f"Playing previous song: {prev_song.title} by {prev_song.artist}")
        return prev_song

    def display_playlist(self):
        if not self.head:
            print("No songs in the playlist.")
            return
        current = self.head
        while current:
            print(f"Song: {current.title} by {current.artist}")
            current = current.next

# Example Usage
if __name__ == "__main__":
    playlist = PlaylistManager()

    # Adding songs
    playlist.add_song("Song 1", "Artist A")
    playlist.add_song("Song 2", "Artist B")
    playlist.add_song("Song 3", "Artist C")

    # Displaying playlist
    print("Playlist:")
    playlist.display_playlist()

    # Playing songs
    current_song = playlist.head
    print(f"\nPlaying current song: {current_song.title} by {current_song.artist}")
    
    # Play next song
    current_song = playlist.play_next(current_song)
    
    # Play next song again
    current_song = playlist.play_next(current_song)
    
    # Try to play next song when at the end of the playlist
    playlist.play_next(current_song)
    
    # Play previous song
    current_song = playlist.play_prev(current_song)
    
    # Play previous song again
    current_song = playlist.play_prev(current_song)
    
    # Try to play previous song when at the beginning of the playlist
    playlist.play_prev(current_song)

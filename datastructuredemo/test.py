import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QListWidget
import pygame

class MusicFile:
    def __init__(self, fileName):
        self.filename = fileName
        self.next = None

class MusicStack:
    def __init__(self):
        self.top: MusicFile = None
        
    def push(self, newtop: MusicFile):
        newtop.next = self.top
        self.top = newtop
    
    def pop(self):
        if self.top.next == None:  
            self.top = None
            print("stack now empty")
            return True
        elif self.top == None: 
            print("stack is ALREADY empty")
            return False
        else:
            self.top = self.top.next
            return True
    
    
    
    
    
    

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        # TODO
        self.playlist: MusicStack = MusicStack()  # Initialize the playlist as an empty list (stack)
        
        # self.currentTrackIndex = None  # Keep track of the currently playing song
        self.isPlaying = False  # Playback state
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Music Player with Playlist')
        self.setGeometry(100, 100, 300, 200)
        
        self.openButton = QPushButton('Open', self)
        self.playButton = QPushButton('Play', self)
        self.nextButton = QPushButton('Next', self)  # Next button to play the next song
        self.stopButton = QPushButton('Stop', self)
        self.playlistWidget = QListWidget(self)
        self.trackLabel = QLabel('No track loaded.', self)

        self.openButton.clicked.connect(self.openFile)
        self.playButton.clicked.connect(self.togglePlayPause)
        self.nextButton.clicked.connect(self.playNext)
        self.stopButton.clicked.connect(self.stopMusic)

        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.playButton)
        layout.addWidget(self.nextButton)
        layout.addWidget(self.stopButton)
        layout.addWidget(self.playlistWidget)
        layout.addWidget(self.trackLabel)

        self.setLayout(layout)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "MP3 Files (*.mp3);;WAV Files (*.wav)")
        if fileName:
            # TODO
            new_data = MusicFile(fileName=fileName)
            self.playlist.push(new_data)
            # self.playlist.append(fileName)  # Add the selected file to the playlist stack
            self.playlistWidget.addItem(fileName.split("/")[-1])  # Display the file name in the playlist widget


    def togglePlayPause(self):
        if not self.playlist:
            self.trackLabel.setText('Playlist is empty.')
            return
        
        if not pygame.mixer.music.get_busy():
            # Play the current track if not already playing
            self.playCurrentTrack()
        else:
            # Pause if music is currently playing
            pygame.mixer.music.pause()
            self.isPlaying = False
            self.playButton.setText('Play')
    
    def playCurrentTrack(self):
        # TODO
        # xoa currentTrackIndex
        # if self.currentTrackIndex is not None:
        #     pygame.mixer.music.load(self.playlist[self.currentTrackIndex])
        #     pygame.mixer.music.play()
        #     self.trackLabel.setText(f'''Now Playing: 
        #         {self.playlist[self.currentTrackIndex].split("/")[-1]}
        #     ''')
        #     self.isPlaying = True
        #     self.playButton.setText('Pause')
        
        if self.playlist.top is not None:
            top_stack = self.playlist.top
            pygame.mixer.music.load(top_stack.filename) 
            self.trackLabel.setText(f'''Now Playing: 
                {top_stack.filename.split("/")[-1]}
            ''')
            self.isPlaying = True
            self.playButton.setText('Pause')
    
    def playNext(self):
        if self.playlist.top is not None:
            # TODO
            # self.currentTrackIndex -= 1  # Move to the next track in the list
            # if self.currentTrackIndex < 0:
            #     self.currentTrackIndex = len(self.playlist) - 1  # Loop back to the start if at the end
            self.playlist.pop()
            self.playCurrentTrack()
    
    def stopMusic(self):
        pygame.mixer.music.stop()
        self.isPlaying = False
        self.playButton.setText('Play')

    def refreshPlaylistDisplay(self):
        self.playlistWidget.clear()  # Clear the current display
        for track in reversed(self.playlist):  # Re-add tracks to display (LIFO order)
            self.playlistWidget.addItem(track.split("/")[-1])

def main():
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

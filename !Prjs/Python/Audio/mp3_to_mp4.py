from moviepy.editor import AudioFileClip, VideoClip, VideoFileClip
import numpy as np


def mp3_to_mp4(input_mp3, output_mp4, resolution=(1, 1), fps=60):

    audio = AudioFileClip(input_mp3)
    
    # Créer une fonction pour générer les images de la vidéo
    def make_frame(t):
        return np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
    
    # Créer un clip vidéo en utilisant la fonction make_frame
    video = VideoClip(make_frame, duration=audio.duration)
    
    # Ajouter l'audio au clip vidéo
    video = video.set_audio(audio)
    
    # Sauvegarder le clip vidéo au format MP4
    video.write_videofile(output_mp4, codec='libx264', fps=fps)
    
    print("Conversion terminée.")

def m4a_to_mp4(input_mp3, output_mp4, resolution=(1, 1), fps=60):
    audio = AudioFileClip(input_mp3)
    
    # Créer une fonction pour générer les images de la vidéo
    def make_frame(t):
        return np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
    
    # Créer un clip vidéo en utilisant la fonction make_frame
    video = VideoClip(make_frame, duration=audio.duration)
    
    # Ajouter l'audio au clip vidéo
    video = video.set_audio(audio)
    
    # Sauvegarder le clip vidéo au format MP4
    video.write_videofile(output_mp4, codec='libx264', fps=fps)
    
    print("Conversion terminée.")
    



if __name__ == "__main__":
    input_mp3 = input("file : ")
    output_mp4 = input_mp3+".mp4"
    if input_mp3.endswith(".m4a"):
        m4a_to_mp4(input_mp3, output_mp4)
    else:
        mp3_to_mp4(input_mp3, output_mp4)

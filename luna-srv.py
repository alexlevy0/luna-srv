import time


def main():
    video_filename = "video.mp4"
    image_filename = "moi.jpg"

    output_filename = (
        f"{video_filename.split('.')[0]}-{image_filename.split('.')[0]}.mp4"
    )

    # command = f"python run.py -s '{image_filename}' -t '{video_filename}' -o '{output_filename}' --keep-fps --output-video-quality 10"
    process = subprocess.Popen(command, shell=True)

    # Attendre la fin de l'exécution de la commande
    process.wait()


if __name__ == "__main__":
    main()

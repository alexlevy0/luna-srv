import time


def main():
    video_filename = "video.mp4"
    image_filename = "moi.jpg"

    output_filename = (
        f"{video_filename.split('.')[0]}-{image_filename.split('.')[0]}.mp4"
    )

    command = f"python run.py -s '{image_filename}' -t '{video_filename}' -o '{output_filename}' --keep-fps --output-video-quality 10"
    # command = "python run.py -h"

    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    # output, error = process.communicate()


if __name__ == "__main__":
    main()

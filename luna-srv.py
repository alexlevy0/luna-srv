def main():
    video_filename = "video.mp4"
    image_filename = "moi.jpg"

    output_filename = (
        f"{video_filename.split('.')[0]}-{image_filename.split('.')[0]}.mp4"
    )

    # command = "python run.py -h"
    command = "python -v"
    # print(f"luna-srv.py cmd : {command}")

    # command = f"python run.py -s '{image_filename}' -t '{video_filename}' -o '{output_filename}' --keep-fps --output-video-quality 10"
    # process = subprocess.Popen(command)
    # process = subprocess.Popen(command, shell=True)

    # process = subprocess.Popen(
    #     command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    # )
    # output, error = process.communicate()
    # print(f"luna-srv.py output : {output}")

    res = subprocess.check_output('ls', shell=True, text=True)
    print(res)

    # result = subprocess.run(["echo", "hello", "world"], capture_output=True, text=True)
    # print(repr(result.stdout))

    # subprocess.run(command, capture_output=True, text=True).stdout
    # print(f"luna-srv.py output : {output_filename}")

    # process.wait()


if __name__ == "__main__":
    main()

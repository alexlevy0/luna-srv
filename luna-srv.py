from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        video_url = query_params.get("videoUrl", [None])[0]
        image_url = query_params.get("imageUrl", [None])[0]

        if not video_url or not image_url:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"")
            return

        image_filename = image_url.split("/")[-1].split(".")[0]
        video_filename = video_url.split("/")[-1].split(".")[0]

        output_filename = f"{video_filename}-{image_filename}.mp4"
        # print(output_filename)

        # command = f"python run.py -s '{image_url}' -t '{video_url}' -o '{output_filename}' --keep-fps --output-video-quality 10"
        # command = "python run.py -h"

        # process = subprocess.Popen(
        #     command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        # )
        # output, error = process.communicate()
        # print(output)
        # print(error)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(output_filename.encode())


def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur le port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

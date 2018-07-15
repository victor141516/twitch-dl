from flask import Flask, request, redirect, send_from_directory, send_file, abort, jsonify
import os
import re
import subprocess
from uuid import uuid4


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/uploads'
twitch_url_regex = re.compile('^https://www.twitch.tv/videos/[0-9]+$')


@app.route('/dl', methods=['GET', 'POST'])
def download_twitch_video():
    url = request.args.get('u', request.form.get('u'))
    if not twitch_url_regex.match(url):
        return 'NOT_VALID_TWITCH_VIDEO_URL'

    exec_line = 'youtube-dl'

    cookies_file = request.files.get('c')
    if cookies_file:
        filename = str(uuid4())
        cookies_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        exec_line += ' --cookies {}/{}'.format(app.config['UPLOAD_FOLDER'], filename)

    exec_line += ' -o - "' + url + '"'
    d_process = subprocess.Popen(exec_line, shell=True, stdout=subprocess.PIPE)

    return send_file(d_process.stdout, as_attachment=True, attachment_filename='video.mp4')


@app.route('/')
def show_form():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 8899, debug=True)

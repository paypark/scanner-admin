#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, jsonify, send_from_directory, send_file

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/increase')
def increase():
    obj = {}
    obj['message'] = "increased"
    return jsonify(obj)

@app.route('/decrease')
def decrease():
    obj = {}
    obj['message'] = "decreased"
    return jsonify(obj)

@app.route('/snapshot', methods = ['PUT'])
def snapshot():
    filename = Camera.snapshot()
    obj = {}
    obj['filename'] = filename
    return jsonify(obj)

@app.route('/snapshot/<path:path>', methods = ['GET'])
def snapshotDetail(path):
    if os.environ.get('CAMERA') == 'pi':
        return send_from_directory('.', path)
    else:
        return send_from_directory('.', '1.jpg')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

#!/usr/bin/env python
from importlib import import_module
import os
import json
from flask import Flask, render_template, Response, jsonify, send_from_directory, send_file, request

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

from CaptureSettings import CaptureSettings
captureSettings = CaptureSettings()
captureSettings.setShutterSpeed(5000)
captureSettings.setFrameRate(60)
captureSettings.setIso(1)
captureSettings.setHeight(480)
captureSettings.setWidth(640)

app = Flask(__name__, static_folder='static')

@app.route('/<path:filename>')
def send_file(filename):
    print('filename')
    print(filename)
    print(app.static_folder)
    return send_from_directory(app.static_folder, filename)

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

@app.route('/settings', methods = ['GET', 'PATCH'])
def settings():
    if request.method == 'GET':
        return jsonify(captureSettings.toJSON())

    if request.method == 'PATCH':
        jsonObject = request.get_json()
        captureSettings.set(jsonObject)
        Camera.updateSettings(captureSettings)
        return json.dumps({ 'success': True }, 200, { 'Content-Type': 'applicaton/json' })

@app.route('/recording/start', methods = ['GET'])
def recordingStart():
    Camera.startRecording()
    return json.dumps({ 'message': 'recording started' }, 200, { 'Content-Type': 'applicaton/json' })

@app.route('/recording/stop', methods = ['GET'])
def recordingStop():
    Camera.stopRecording()
    return json.dumps({ 'message': 'recording stopped' }, 200, { 'Content-Type': 'applicaton/json' })

@app.route('/recording/is-recording', methods = ['GET'])
def recordingIsRecording():
    isRecording = Camera.isCameraRecording()
    return json.dumps({ 'isRecording': isRecording }, 200, { 'Content-Type': 'applicaton/json' })

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        gen(Camera(captureSettings)),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

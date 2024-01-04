from flask import Flask, request
from flask_cors import CORS
import os
import serial
import time

printerAPI = Flask(__name__)
CORS()
gcode_folder = "gcodeFolder"
printerAPI.config["GCodeFolder"] = gcode_folder
if os.path.exists("GCodeFolder") == False:
    os.makedirs("GCodeFolder")
cereal=serial.Serial('/dev/ttySo', baudrate = 115200, timeout=1)
cereal.open()
@printerAPI.route("/api/printer", methods=["POST"])
def printerFile():
    if 'gcode_file' not in request.files:
        return 'No file uploaded'

    gcode_file = request.files['gcode_file']

    if gcode_file.filename == '':
        return 'No file'

    if gcode_file:
        gcode_fp = os.path.join(printerAPI.config["GCodeFolder"], gcode_file.filename)
        gcode_file.save(gcode_fp)
        cereal.write(b"M23 gcode_file.filename\n")
        print("good :)")
    return 'good :)'

@printerAPI.route("/api/printer/start")
def start():
    cereal.write(b"M24\n")

@printerAPI.route("/api/printer/stop")
def start():
    cereal.write(b"M25\n")

@printerAPI.route("/api/printer/autohome")
def start():
    cereal.write(b"G28\n")

if __name__ == '__main__':
    printerAPI.run(debug=True)
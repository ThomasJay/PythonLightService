import asyncio
from kasa import SmartPlug
from flask import Flask, request, jsonify

app = Flask(__name__)

api_v1_prefix = "/api/v1/"


PLUG_IP = "10.10.10.33"


async def light_on():
    plug = SmartPlug(PLUG_IP)
    await plug.update()
    await plug.turn_on()


async def light_off():
    plug = SmartPlug(PLUG_IP)
    await plug.update()
    await plug.turn_off()


@app.route("/", methods=["GET"])
def get_home():
    return "Light Microservice"


@app.route(api_v1_prefix + "/health", methods=["GET"])
def get_health():
    return jsonify({"status": "Healthy"}), 200, {"Content-Type": "application/json"}


@app.route(api_v1_prefix + "/off", methods=["GET"])
def get_off():
    asyncio.run(light_off())

    return jsonify({"status": "Light Off"}), 200, {"Content-Type": "application/json"}


@app.route(api_v1_prefix + "/on", methods=["GET"])
def get_on():
    asyncio.run(light_on())

    return jsonify({"status": "Light On"}), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8086)  # Auto reload

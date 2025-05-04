from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    amp_ip = "192.168.10.2"
    vol_min = 0
    vol_max = 60
    vol_default = 30

    channel = {
        "Blu-ray/DVD": {
            "view": True,
            "name": "Blu-ray/DVD",
            "cmd": "SIBD",
        },
        "TV Audio": {
            "view": False,
            "name": "TV Audio",
            "cmd": "SITV",
        },
        "CBL/SAT": {
            "view": False,
            "name": "CBL/SAT",
            "cmd": "SISAT/CBL",
        },
        "Game": {
            "view": False,
            "name": "Game",
            "cmd": "SIGAME",
        },
        "AUX": {
            "view": False,
            "name": "AUX",
            "cmd": "SIAUX1",
        },
        "Tuner": {
            "view": False,
            "name": "Tuner",
            "cmd": "SITUNER",
        },
        "CD": {
            "view": False,
            "name": "CD",
            "cmd": "SICD",
        },
        "Media Player": {
            "view": True,
            "name": "Media Player",
            "cmd": "SIMPLAY",
        },
        "Phono": {
            "view": False,
            "name": "Phono",
            "cmd": "SIPHONO",
        },
        "HDMI1": {
            "view": False,
            "name": "HDMI1",
            "cmd": "SIHDP",
        },
        "HDMI2": {
            "view": False,
            "name": "HDMI2",
            "cmd": "SIHDMI2",
        },
    }

    visible_channels = {k: v for k, v in channel.items() if v["view"]}

    return render_template(
        "index.html",
        amp_ip=amp_ip,
        vol_min=vol_min,
        vol_max=vol_max,
        vol_default=vol_default,
        channel=visible_channels,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

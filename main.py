from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    amp_ip = "192.168.10.2"
    vol_min = 0
    vol_max = 60
    vol_default = 30
    return render_template('index.html', amp_ip=amp_ip, vol_min=vol_min, vol_max=vol_max, vol_default=vol_default)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)

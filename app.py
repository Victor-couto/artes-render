from flask import Flask, request, jsonify, render_template
import json, os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ A.R.T.E.S. online na nuvem (Render)"

@app.route("/start", methods=["POST"])
def start():
    return jsonify({"status": "A.R.T.E.S. iniciado (simulação)"})

@app.route("/stop", methods=["POST"])
def stop():
    return jsonify({"status": "A.R.T.E.S. interrompido (simulação)"})

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "saldo": 10042.57,
        "taxa_acerto_total": 0.73,
        "agente_ativo": "PPO",
        "trades_hoje": 42
    })

@app.route("/config", methods=["POST"])
def config():
    data = request.json
    with open("config.json", "w") as f:
        json.dump(data, f, indent=2)
    return jsonify({"status": "Parâmetros atualizados", "config": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

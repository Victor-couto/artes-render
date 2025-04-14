import time, json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def simulate_agent():
    print("🔁 A.R.T.E.S. executando... (simulação)")
    config = load_config()
    print(f"Exposição: {config['exposure_pct']*100}%, Risco: {config['risk_pct']*100}%")
    while True:
        time.sleep(10)
        print("📈 Simulando decisão e ação do agente...")

if __name__ == "__main__":
    simulate_agent()

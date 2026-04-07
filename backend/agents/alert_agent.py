
from config import GAS_THRESHOLD

def alert_agent(data):
    gas = data.get("gas", 0)

    if gas > GAS_THRESHOLD:
        return {"alert": f"⚠️ Gas HIGH: {gas}"}
    
    return {"alert": "Gas normal"}

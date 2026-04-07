
def env_agent(data):
    return {
        "temperature": data.get("temperature"),
        "humidity": data.get("humidity")
    }

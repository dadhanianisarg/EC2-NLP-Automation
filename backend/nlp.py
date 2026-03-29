def parse_user_input(text):
    text = text.lower()

    config = {
        "instance_type": "t3.micro",   # ✅ FORCE
        "region": "ap-south-1",
        "os": "ubuntu",
        "ports": []
    }

    if "amazon linux" in text:
        config["os"] = "amazon-linux"

    if "ssh" in text:
        config["ports"].append(22)
    if "http" in text:
        config["ports"].append(80)
    if "https" in text:
        config["ports"].append(443)

    return config
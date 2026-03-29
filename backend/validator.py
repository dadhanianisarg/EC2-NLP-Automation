# backend/validator.py

def validate(config):
    if "instance_type" not in config:
        raise Exception("Invalid config")

    return config
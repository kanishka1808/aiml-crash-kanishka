# day5 task6 --JSON Config Manager

import json


def save_config(data: dict, filename: str):
    """Saves a dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_config(filename: str) -> dict:
    """Loads and returns data from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)


def update_config(filename: str, key: str, value):
    """Updates a key in the JSON file and saves it."""
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)


# Initial configuration
config_data = {
    "model": "RandomForest",
    "learning_rate": 0.01,
    "epochs": 10
}

# Save config
save_config(config_data, "config.json")

# Update epochs
update_config("config.json", "epochs", 20)

# Load and display updated config
updated_config = load_config("config.json")
print(updated_config)

# Explore Section:
# json.dump() writes Python data directly to a file.
# json.dumps() converts Python data into a JSON string.
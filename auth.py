import json
import hashlib

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("users.json is corrupted. Resetting it.")
        return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def sign_up(username, password):
    users = load_users()
    if username in users:
        return False, "Username already exists."
    users[username] = {"password": hash_password(password), "high_score": 0}
    save_users(users)
    return True, "Sign-up successful."

def update_high_score(username, score):
    users = load_users()
    if username in users:
        if score > users[username]["high_score"]:
            users[username]["high_score"] = score
            save_users(users)

def get_high_score(username):
    users = load_users()
    return users.get(username, {}).get("high_score", 0)


def log_in(username, password):
    users = load_users()
    if username not in users:
        return False, "User not found."
    if users[username]["password"] != hash_password(password):
        return False, "Incorrect password."
    return True, "Login successful."




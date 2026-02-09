from datetime import datetime

# -----------------------------
# Simulated backend data store
# -----------------------------
USERS_DB = {
    "U001": {
        "name": "Harini",
        "emergency_contacts": [
            "contact1@example.com",
            "contact2@example.com"
        ],
        "safe_zones": ["Home", "Office"]
    }
}

# -----------------------------
# SOS Event Handler
# -----------------------------
def handle_sos_event(user_id, situation, silent_mode=False):
    user = USERS_DB.get(user_id)
    if not user:
        print("[ERROR] User not found")
        return

    location = fetch_current_location()
    media_file = media_decision_engine(situation, silent_mode)

    notify_contacts(
        user["emergency_contacts"],
        user["name"],
        location,
        situation,
        media_file
    )

    print(f"\n[SOS LOG] User: {user['name']} | Situation: {situation} | Silent: {silent_mode}")

# -----------------------------
# Location Service (Mock)
# -----------------------------
def fetch_current_location():
    return "12.9716° N, 77.5946° E"

# -----------------------------
# Media Decision Logic
# -----------------------------
def media_decision_engine(situation, silent_mode):
    if situation == "walking_alone":
        media_type = "audio_video"
    else:
        media_type = "audio_only"

    if silent_mode:
        print("[Decoy Mode] Background recording")
    else:
        print("[Normal Mode] Recording active")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{media_type}_{timestamp}.mp4"

# -----------------------------
# Alert Dispatcher
# -----------------------------
def notify_contacts(contacts, username, location, situation, media):
    for contact in contacts:
        print(
            f"Alert sent to {contact} | "
            f"User: {username} | "
            f"Location: {location} | "
            f"Situation: {situation} | "
            f"Media: {media}"
        )

# -----------------------------
# Simulation Scenarios
# -----------------------------
handle_sos_event(
    user_id="U001",
    situation="walking_alone",
    silent_mode=True
)

handle_sos_event(
    user_id="U001",
    situation="public_place",
    silent_mode=False
)

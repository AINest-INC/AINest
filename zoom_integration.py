# zoom_integration.py
import requests
import json

# Replace with your Zoom API credentials
ZOOM_API_KEY = "YOUR_ZOOM_API_KEY"
ZOOM_API_SECRET = "YOUR_ZOOM_API_SECRET"

def create_zoom_meeting(topic, start_time, duration):
    """Creates a Zoom meeting using the Zoom API."""
    url = "https://api.zoom.us/v2/users/me/meetings"
    headers = {
        "Authorization": f"Bearer {generate_jwt_token(ZOOM_API_KEY, ZOOM_API_SECRET)}",
        "Content-Type": "application/json"
    }
    data = {
        "topic": topic,
        "type": 2,  # Scheduled meeting
        "start_time": start_time,
        "duration": duration,
        "settings": {
            "host_video": True,
            "participant_video": False,
            "join_before_host": True,
            "mute_upon_entry": True
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error creating Zoom meeting: {response.status_code} - {response.text}")
        return None

def generate_jwt_token(api_key, api_secret):
    """Generates a JWT token for Zoom API authentication."""
    import jwt
    import time
    payload = {
        'iss': api_key,
        'exp': int(time.time()) + 3600  # Token expires in 1 hour
    }
    jwt_token = jwt.encode(payload, api_secret, algorithm='HS256')
    return jwt_token

if __name__ == '__main__':
    # Example usage
    meeting_details = create_zoom_meeting(
        topic="AiNest Demo Meeting",
        start_time="2024-01-01T10:00:00Z",  # ISO 8601 format
        duration=60
    )
    if meeting_details:
        print("Zoom Meeting Created:")
        print(json.dumps(meeting_details, indent=4))
    else:
        print("Failed to create Zoom meeting.")

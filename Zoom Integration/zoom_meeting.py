# zoom_meeting.py
import requests
import json

def create_zoom_meeting(topic, start_time, duration, api_key, api_secret):
    """Creates a Zoom meeting.

    Args:
        topic (str): The topic of the meeting.
        start_time (str): The start time of the meeting (YYYY-MM-DDTHH:MM:SSZ).
        duration (int): The duration of the meeting in minutes.
        api_key (str): Your Zoom API key.
        api_secret (str): Your Zoom API secret.

    Returns:
        dict: The meeting details if successful, None otherwise.
    """
    url = "https://api.zoom.us/v2/users/me/meetings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {generate_jwt_token(api_key, api_secret)}"
    }
    payload = json.dumps({
        "topic": topic,
        "type": 2,  # Scheduled meeting
        "start_time": start_time,
        "duration": duration,
        "settings": {
            "host_video": True,
            "participant_video": True,
            "join_before_host": True,
            "mute_upon_entry": False
        }
    })

    response = requests.post(url, headers=headers, data=payload)

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
    # Example usage:
    api_key = "YOUR_ZOOM_API_KEY"
    api_secret = "YOUR_ZOOM_API_SECRET"
    meeting_details = create_zoom_meeting(
        topic="AiNest Demo Meeting",
        start_time="2024-01-01T10:00:00Z",
        duration=60,
        api_key=api_key,
        api_secret=api_secret
    )

    if meeting_details:
        print("Zoom meeting created successfully:")
        print(json.dumps(meeting_details, indent=4))
    else:
        print("Failed to create Zoom meeting.")

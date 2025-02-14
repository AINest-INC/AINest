# zoom_integration.py
from zoom_meeting import create_zoom_meeting

def schedule_meeting(topic, start_time, duration, api_key, api_secret):
    """Schedules a Zoom meeting using the zoom_meeting module.

    Args:
        topic (str): The topic of the meeting.
        start_time (str): The start time of the meeting (YYYY-MM-DDTHH:MM:SSZ).
        duration (int): The duration of the meeting in minutes.
        api_key (str): Your Zoom API key.
        api_secret (str): Your Zoom API secret.

    Returns:
        dict: The meeting details if successful, None otherwise.
    """
    return create_zoom_meeting(topic, start_time, duration, api_key, api_secret)

if __name__ == '__main__':
    # Example usage:
    api_key = "YOUR_ZOOM_API_KEY"
    api_secret = "YOUR_ZOOM_API_SECRET"
    meeting = schedule_meeting(
        topic="AiNest Integration Meeting",
        start_time="2024-01-02T14:00:00Z",
        duration=45,
        api_key=api_key,
        api_secret=api_secret
    )

    if meeting:
        print("Meeting scheduled successfully:")
        print(meeting)
    else:
        print("Failed to schedule meeting.")

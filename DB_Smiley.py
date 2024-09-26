import googleapiclient.discovery
import pandas as pd

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "your api key"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

# List of video IDs
video_ids = ["D1iVoUe13zc", "BHBn7Zm1nR8", "49D_B52UQwk", "KVcyoOSXtmA", "zq4t-Wl0jr4"]

# List of specified emojis
specified_emojis = ['😂', '😁', '😃', '😅', ':)', '🤣', '😄', '😆', '😊', '☺', '🙂', '😌', '😜', '😝', ':d' ]

comments = []

for video_id in video_ids:
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    # Execute the request.
    response = request.execute()

    # Get the comments from the response.
    while True:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            text = comment['textOriginal']
            public = item['snippet']['isPublic']

            # Check if the comment contains any specified emoji
            if any(emoji in text for emoji in specified_emojis):
                comments.append([
                    0,  # Add ID to the row
                    text,
                ])

        try:
            nextPageToken = response['nextPageToken']
        except KeyError:
            break

        # Create a new request object with the next page token.
        nextRequest = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100,
                                                    pageToken=nextPageToken)
        # Execute the next request.
        response = nextRequest.execute()

# Create DataFrame with added 'Video_ID' column
df = pd.DataFrame(comments, columns=['ID', 'comment'])

# Write DataFrame to Excel file
df.to_excel('DB_smiley.xlsx', index=False)

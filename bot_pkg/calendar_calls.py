from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime, timedelta

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'path_to_file/credentials.json'
DAYS_DELTA = 1
DATETIME_TEMPLATE = '%Y-%m-%dT%H:%M:%S'  # 2018-09-03T14:10:00+03:00


def get_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def list_events():
    service = get_service()
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    end_date = (datetime.utcnow() + timedelta(days=DAYS_DELTA)).isoformat() + 'Z'
    print('Getting List of 10 events')
    events_result = service.events().list(
        calendarId='primary', timeMin=now, timeMax=end_date, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items')
    res = []

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime')
        dt = datetime.strptime(start[:-6], DATETIME_TEMPLATE)  # 2018-09-03T14:10:00+03:00
        end = event['end'].get('dateTime')
        dt_end = datetime.strptime(end[:-6], DATETIME_TEMPLATE)
        res.append((dt, event['summary'], dt_end))
    return res  # [(start, summary, end),...]


if __name__ == '__main__':
    list_events()
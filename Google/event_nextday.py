from cal_setup import get_calendar_service

def get_events():
    service = get_calendar_service()

    # To get list of calendars and it's ids uncomment next code
    # calendars_result = service.calendarList().list().execute()
    # calendars = calendars_result.get('items', [])
    # for cal in calendars:
    #   print(cal['summary'], "id:", cal['id'])

    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    end_date = (datetime.utcnow() + timedelta(days=DAYS_DELTA)).isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary',
                                          timeMin=now, timeMax=end_date,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items')
    res = []
    for event in events:
        start = event['start'].get('dateTime')
        dt = datetime.strptime(start[:-6], DATETIME_TEMPLATE)  # 2018-09-03T14:10:00+03:00
        end = event['end'].get('dateTime')
        dt_end = datetime.strptime(end[:-6], DATETIME_TEMPLATE)
        res.append((dt, event['summary'], dt_end))
    return res # [(start, summary, end),...]


if __name__ == '__main__':
    get_events()


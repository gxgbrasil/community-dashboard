class Filter:

    def group_basic_info(self, group_data):
        group_info = {'id':         group_data['id'],
                      'name':       group_data['name'],
                      'urlname':       group_data['urlname'],
                      'created':    group_data['created']}
        return group_info

    def events(self, events_data):
        events_list = []
        events_result = events_data['results']

        for event in events_result:
            event_details = {'id': event['id'],
                             'audience': event['yes_rsvp_count'],
                             'created': event['created'],
                             'utc_offset': event['utc_offset'],
                             'duration': event['time']}
            events_list.append(event_details)

        return events_list

    def rsvps(self, rsvps_data):
        attendees = []

        for rsvp in rsvps_data:
            if rsvp['response'] == 'yes':
                attendees.append(rsvp['member']['id'])

        return attendees

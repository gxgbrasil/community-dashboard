class Filter:

    def group_basic_info(self, group_data):
        group_info = {'id': group_data['id'], 'name': group_data['name'], 'members': group_data['members']}
        return group_info

    def events(self, events_data):
        events_list = []
        events_result = events_data['results']

        for event in events_result:
            events_list.append(event['id'])

        return events_list

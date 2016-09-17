*Endpoints*

- Group (/:urlname)
    - ID (id)
    - Name (name)
    - Create date (created)
- Events (/2/events)
    - ID
    - Audience: yes_rsvp_count
    - Create date: created (add: utc_offset)
    - Duration (time)
- Members (/members)
    - Topics
    - Joined
    - ID
- RSVPs (/2/events/:event_id/rsvps)
    - Member ID (member/id)
    - *Response (response with value ‘yes')

*Graphs*

MVP 1

Display

[ ] Number of days

[ ] Number of events

[ ] Mean of attendees

[ ] Number of members

Graphs

[ ] Events by Day (event create date - day of week)

[ ] Attendees by Gender (use genderize.io to get by name - count by gender by join month)

[ ] Top 5 Interests Topics (get topics, capitalize and count)

[ ] Newest and Frequents Attendees (calculate join_date - event_date, to each event; if the result is greater than 3, it’s an older member - group by month)
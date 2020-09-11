#defining event class
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines={}
    for event in events:
        #if the current machine doesnot have a key value
        #pair in the dict it is added
        if event.machine not in machines:
            machines[event.machine]=set()

        #depending on user is removed or added from machine
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            if event.user not in machines[event.machine]:
                continue
            machines[event.machine].remove(event.user)

        return machines

def generate_report(machines):
    for machine,users in machines.items():
        if len(users) > 0:
            user_list =','.join(users)
            print(f"{machine}: {user_list}")

#driver code
#making a list of event objects
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]
users= current_users(events)
#users is now a dict containing all present users
generate_report(users)





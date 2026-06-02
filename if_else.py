# Dictionary of IT incidents with ticket numbers as keys and priorities as values
# Priority levels: 1 = High, 2 = Medium, 3 = Low

it_incidents = {
    1001: 1,  # High priority incident
    1002: 2,  # Medium priority incident
    1003: 3,  # Low priority incident
    1004: 1,  # High priority incident
    1005: 2,  # Medium priority incident
    1006: 3,  # Low priority incident
}

# loops through the dict and list each priority by ticket
for inc, priority in it_incidents.items():
    if priority == 1:
        print(f'Incident {inc} is High priority')
    elif priority == 2:
        print(f'Incident {inc} is Medium priority')
    elif priority == 3:
        print(f'Incident {inc} is Low priority')
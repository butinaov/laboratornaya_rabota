def find_common_participants(group1, group2, argument=","):

    participants1 = set(group1.split(argument))
    participants2 = set(group2.split(argument))

    common_participants = participants1.intersection(participants2)

    common_participants.sort()

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, argument="|")
print(common_participants)

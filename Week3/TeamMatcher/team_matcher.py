import requests
import re


def get_courses(people):
    courses = set()
    for person in people:
        for cours in person['courses']:
            courses.add(cours['name'])
    return list(courses)


def print_courses(available_courses):
    for index in range(len(available_courses)):
        print("[{}] {} ".format(str(index + 1), available_courses[index]))


def get_available_people(people, available_courses, course_id, group_time):
    available_people = []
    for person in people:
        if person["available"] and \
           int(group_time) in [x["group"] for x in person["courses"]] and \
           available_courses[course_id] in [x["name"] for x in person["courses"]]:

            available_people.append(person)

    return available_people


def main():
    r = requests.get("https://hackbulgaria.com/api/students/",
                     verify=False)
    people = r.json()

    print([x["group"] for x in people[0]["courses"]])
    print([x["name"] for x in people[0]["courses"]])

    print("Hello, you can use one of the following commands: ")
    print('"list courses" - this lists all the courses that are available now')
    print('"match teams" -  <course_id>, <team_size>, <group_time>')
    print('"exit" - Exit the program')

    available_courses = get_courses(people)
    command = input("Type command: ")

    while(command != 'exit'):

        if command == "list courses":
            print_courses(available_courses)

        if "match teams" in command or "rematch" in command:
            stats = re.findall(r'\d+', command)
            print(get_available_people(people,
                                       available_courses,
                                       int(stats[0]) - 1,
                                       stats[2]))

        command = input("Type command: ")


if __name__ == "__main__":
    main()

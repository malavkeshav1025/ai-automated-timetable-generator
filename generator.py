import sqlite3
import random

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

SLOTS = [
    "10-11",
    "11-12",
    "12-1",
    "2-3",
    "3-4"
]

def generate_timetable():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    subjects = cursor.execute(
        "SELECT name, faculty FROM subjects"
    ).fetchall()

    conn.close()

    timetable = {}

    for day in DAYS:

        timetable[day] = {}

        used_faculty = []

        for slot in SLOTS:

            available_subjects = []

            for sub in subjects:

                subject_name = sub[0]
                faculty_name = sub[1]

                if faculty_name not in used_faculty:

                    available_subjects.append({
                        'subject': subject_name,
                        'faculty': faculty_name
                    })

            if available_subjects:

                available_subjects.sort(
                    key=lambda x: x['subject']
                )

                chosen = random.choice(
                    available_subjects
            )

                timetable[day][slot] = chosen

                used_faculty.append(
                    chosen['faculty']
                )

            else:

                timetable[day][slot] = {
                    'subject': 'FREE',
                    'faculty': '-'
                }

    return timetable
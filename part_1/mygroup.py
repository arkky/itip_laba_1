def filterStudents(gpa: int):
    for student in groupmates:
        marks = student["marks"]
        mean = round(sum(marks) / len(marks), 2)
        if mean >= gpa:
            string = f"{student['name']} {student['surname']}\nОценки: {marks}\nСредний балл: {mean}"
            print(string)
            print()

groupmates = [
    {
        "name": "Александр",
        "surname": "Каргашинский",
        "exams": ["ИТИП", "ИСИС", "МСИС"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Родичев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Евгений",
        "surname": "Зуев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Руслан",
        "surname": "Магомедов",
        "emaxs": ["Физкультура", "МСИ", "БЖД"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Алексей",
        "surname": "Новиков",
        "exams": ["МСИС", "МТИП", "МСИП"],
        "marks": [3, 4, 3]
    }
]


if __name__ == "__main__":
    try:
        gpa = int(input("Введите минимальный средний балл для студента: "))
        if gpa < 1 and gpa > 5:
            raise
    except:
        print("Неправильно! Введите число от 1 до 5")
    filterStudents(gpa)

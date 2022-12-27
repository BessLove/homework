class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_rating(self) -> float:
        """Расчет средней оценки студента"""
        lst = [self.grades[elem] if type(self.grades[elem]) != list \
                   else sum(self.grades[elem]) / len(self.grades[elem]) for elem in self.grades]
        return sum(lst) / len(lst)

    # def add_courses(self, course_name):
    #     self.finished_courses.append(course_name)

    def garde_lectors(self, lector, course, grade):
        """Оцениваем лектора"""
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_rating()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __eq__(self, other) -> bool:
        return self.average_rating() == other.average_rating()

    def __lt__(self, other) -> bool:
        return self.average_rating() < other.average_rating()

    def __le__(self, other) -> bool:
        return self.average_rating() <= other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.courses = []
        self.grades = {}


    def lectors_avrating(self):
        if not self.grades:
            return 0
        lst = [self.grades[elem] if type(self.grades[elem]) != list else sum(self.grades[elem]) / len(self.grades[elem])
               for elem in self.grades]
        return sum(lst) / len(lst)

    def __eq__(self, other) -> bool:
        return self.lectors_avrating() == other.lectors_avrating()

    def __lt__(self, other) -> bool:
        return self.lectors_avrating() < other.lectors_avrating()

    def __le__(self, other) -> bool:
        return self.lectors_avrating() <= other.lectors_avrating()

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Средняя оценка за лекцию: {self.lectors_avrating()}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """"Выставляем оценки студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'{super().__str__()}'

def avegrade_allstud(persons: list, course: str):
    if not isinstance(persons, list):
        return "Not list"
    grade_lst = []
    for person in persons:
        grade_lst.extend(person.grades.get(course, []))
    if not grade_lst:
        return "По такому курсу ни у кого нет оценок"
    return sum(grade_lst)/len(grade_lst)

'''def ...(persons, course):
    if not isinstance(persons, list):
        return "Not list"
    ... = [] #Определяем пустой список, куда будем складывать оценки (обычная переменная без `self`)
    for person in persons:
        <список>.extend(person.<атрибут с оценками>.get(<курс>, [])) #Используя extend, добавляем оценки в список. Также используем метод get к словарю с оценками с дефолтным значением [], чтобы исключить ошибку в случае, если студент еще не получал оценок по данному курсу
    if not ...: Проверям не пустой ли список
        return "По такому курсу ни у кого нет оценок"
    return round(#Сумму оценок списка делим на длину списка (для этого используем "sum" и "len"), 2)

Если атрибут, содержащий оценки, у классов назван одинаково (например self.grades у обоих классов), то данная функция станет универсальной и сможет принимать как список студентов, так и список лекторов'''


student1 = Student('Ruoy', 'Eman', 'male')  # создали студента
student1.courses_in_progress += ['Python', 'Java']  # добавили этому экземпляру курс для изучения

student2 = Student('John', 'Connor', 'male')  # создали студента
student2.courses_in_progress += ['Python', 'Java', 'C++']  # добавили этому экземпляру курс для изучения

lector1 = Lecturer("Иван", "Иванов")  # создали лектора
lector1.courses += ['Python']

lector2 = Lecturer("Семен", "Петров")  # создали лектора
lector2.courses += ['Python', 'Java', 'C++']

rewiever1 = Reviewer('Евгений', 'Булкин')  #Создали наблюдателя
rewiever1.courses_attached += ['Python', 'Java', 'C++']

rewiever2 = Reviewer('Андрей', 'Вилкин')
rewiever2.courses_attached += ['Python', 'Java', 'C++']



student1.garde_lectors(lector1, 'Python', 10)
student1.garde_lectors(lector2, 'Java', 3)

student2.garde_lectors(lector1, 'Python', 10)
student2.garde_lectors(lector2, 'C++', 3)

rewiever1.rate_hw(student1, 'Python', 10)
rewiever1.rate_hw(student2, 'Java', 10)


rewiever2.rate_hw(student1, 'Python', 10)
rewiever2.rate_hw(student2, 'Java', 9)




print(student1)
print()
print(student2)
print()
print(lector1)
print()
print(lector2)
print()
print(rewiever1)
print()
print(rewiever2)
print()



if student1 > student2:
    print('Средние оценки первого студента выше, чем у второго студента')

if student1 < student2:
    print('Средние оценки первого студента ниже, чем у второго студента')

if student1 == student2:
    print('Средние оценки первого студента и второго студента равны')


if lector1 > lector2:
    print('Средние оценки первого лектора выше, чем у второго лектора')

if lector1 < lector2:
    print('Средние оценки первого лектора ниже, чем у второго лектора')

if lector1 == lector2:
    print('Средние оценки первого лектора и второго лектора равны')

print()


print(avegrade_allstud([student1, student2], "Java"))




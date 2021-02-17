from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subjects(models.Model):
    name = models.CharField("Название дисциплины", max_length=45)

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    def __str__(self):
        return self.name

class Speciality(models.Model):
    name = models.CharField("Название специальности", max_length=45)
    subjects = models.ManyToManyField(Subjects)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name

class Teachers(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    last_name = models.CharField("Фамилия", max_length=20)
    middle_name = models.CharField("Отчество", max_length=20)
    TEACHER = 'T'
    SENIORLECTURER = 'SL'
    TEACHER_POSITIONS_CHOICES = (
        (TEACHER, 'Преподаватель'),
        (SENIORLECTURER, 'Старший Преподаватель')
    )
    position = models.CharField(max_length=2, choices=TEACHER_POSITIONS_CHOICES, default=TEACHER, verbose_name='Должность')
    user_id = models.ForeignKey(User, null=True , on_delete=models.CASCADE, blank=True, verbose_name= 'Аккаунт')
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Classrooms(models.Model):
    name = models.CharField("Номер аудитории", max_length=5)
    LECTURE = 'L'
    PRAСTICAL = 'P'
    CLASSROOMS_CHOICES = (
        (LECTURE, 'Лекционная'),
        (PRAСTICAL, 'Практическая')
    )
    type = models.CharField(max_length=2, choices=CLASSROOMS_CHOICES, default=LECTURE)

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"

    def __str__(self):
        return self.name + " " + self.type

class Groups(models.Model):
    name = models.CharField("Номер группы", max_length=10)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField("Имя",max_length=20)
    last_name = models.CharField("Фамилия",max_length=20)
    middle_name = models.CharField("Отчество",max_length=20)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.last_name + " " + self.first_name

class Couple(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name="Предмет")
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, verbose_name="Преподаватель")
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name="Группа")
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    DAY_CHOICES = (
        (MONDAY, "Понедельник"),
        (TUESDAY, "Вторник"),
        (WEDNESDAY, "Среда"),
        (THURSDAY, "Четверг"),
        (FRIDAY, "Пятница"),
        (SATURDAY, "Суббота"),
        (SUNDAY, "Воскресенье")
    )
    day_week = models.CharField( max_length=3, choices=DAY_CHOICES, default=MONDAY, verbose_name="День недели")
    couple_n = models.IntegerField("Номер пары")
    classroom_id = models.ForeignKey(Classrooms, verbose_name="Аудитория",  on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.couple_n, self.day_week, self.subject_id, self.teacher_id,  self.classroom_id)
               # + " " + self.teacher_id + " " + self.day_week + " " + self.classroom_id


# class DurationSubjects(models.Model):
#     speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE)
#     subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
#     duration = models.IntegerField("Длительность")
#
#     class Meta:
#         verbose_name = ""
#         verbose_name_plural = "Перечень предметов"
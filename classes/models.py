from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)
    # tags = models.ManyToManyField(Tag, related_name='tage')

class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, related_name='lecture_course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE, related_name='Lecture_slide', primary_key=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE, related_name='lecture_assignment', primary_key=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, related_name="course_tag")


    def __str__(self):
        return self.name

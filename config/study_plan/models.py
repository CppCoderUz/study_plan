from django.db import models
from moderator.models import MainUser

class Cafedra(models.Model):
    ''' Kafedra '''
    name = models.CharField(max_length=150, verbose_name='Kafedra nomi')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = '1. Kafedralar'


class Science(models.Model):
    ''' Fan '''
    name = models.CharField(max_length=150, verbose_name='Fan nomi')
    cafedra = models.ForeignKey(Cafedra, on_delete=models.SET_NULL, null=True, verbose_name='Kafedra')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = '2. Fanlar'


class Faculty(models.Model):
    ''' Fakultet '''
    name = models.CharField(max_length=100, verbose_name='Fakultet nomi')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = '3. Fakultetlar'



class Direction(models.Model):
    ''' Yo'nalish '''
    TYPE_CHOICES = (
        ('kunduzgi', 'Kunduzgi'),
        ('sirtqi', 'Sirtqi'),
        ('kechki', 'Kechki')
    )

    name = models.CharField(max_length=100, verbose_name='Yo\'nalish nomi')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_DEFAULT, default=1, verbose_name='Fakultet')
    education_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='kunduzgi', verbose_name='Ta\'lim turi')
    study_time = models.IntegerField(default=4, verbose_name='O\'qish muddati')
    direction_code = models.IntegerField(verbose_name='Yo\'nalish kodi')
    admission_year = models.IntegerField(verbose_name='Qabul qilingan yil')


    def __str__(self) -> str:
        return '%s (%s)' %(self.name, self.education_type)
    
    class Meta:
        verbose_name = 'Yo\'nalish'
        verbose_name_plural = '4. Yo\'nalishlar'


class StudyPlan(models.Model):
    EXAM_TYPE_CHOICES = (
        ('imtihon', 'Imtihon'),
        ('sinov', 'Sinov')
    )
    
    # Fanga oid ma'lumotlar 
    science_code = models.CharField(max_length=20, verbose_name='Fan kodi')
    science = models.ForeignKey(Science, on_delete=models.CASCADE, verbose_name='Fan nomi')
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE_CHOICES, verbose_name='Yakuniy nazorat turi')
    lesson_time = models.IntegerField(verbose_name='Umumiy dars soati')
    
    # Dars soatlari
    lecture_time = models.IntegerField(default=0, verbose_name='Ma\'ruza vaqti')
    practice_time = models.IntegerField(default=0, verbose_name='Amaliyot vaqti')
    seminar_time = models.IntegerField(default=0, verbose_name='Seminar vaqti')
    laboratory_time = models.IntegerField(default=0, verbose_name='Labaratoriya vaqti')
    
    # mustaqil ta'lim
    independent_education_time = models.IntegerField(default=0, verbose_name='Mustaqil ta\'lim')

    # Kurs ishi va malakaviy amaliyot
    professional_practice_time = models.IntegerField(default=0, verbose_name='Malakaviy amaliyot')
    course_work_time = models.IntegerField(default=0, verbose_name='Kurs ishi')

    # Qo'shimcha
    study_semestr = models.IntegerField(verbose_name='O\'quv semestr raqami')
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Yo\'nalish')


    def __str__(self) -> str:
        return '%s - yo\'nalish rejasi (%s - fan)'%(self.direction.name, self.science.name)
    
    class Meta:
        verbose_name = 'Fan rejasi'
        verbose_name_plural = '5. Rejalar'




































# 
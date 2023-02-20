from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Moderator 
from .models import MainUser


# Study Plan
from study_plan.models import (
    Cafedra,
    Science,
    Faculty,
    Direction,
    StudyPlan,
)


admin.site.unregister(Group)


class MainUserAdmin(UserAdmin):
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
admin.site.register(MainUser, MainUserAdmin)



class CafedraAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Cafedra, CafedraAdmin)


class ScienceAdmin(admin.ModelAdmin):
    list_display = ['name', 'cafedra', 'pk']
admin.site.register(Science, ScienceAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Faculty, FacultyAdmin)

class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty','education_type', 'study_time', 'direction_code', 'admission_year', 'pk']
admin.site.register(Direction, DirectionAdmin)


class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['science', 'science_code', 'exam_type', 'lesson_time', 'independent_education_time', 'direction', 'study_semestr']
    fieldsets = (
        (
            _("Fanga oid ma'lumotlar"), {
                "fields": ("science_code", "science", "exam_type")
            }
        ),
        (
            _("Dars soatlari"), {
                "fields": ("lesson_time", "lecture_time", "practice_time", "seminar_time", "laboratory_time")
            }
        ),
        (
            _("Kurs ishi va malakaviy amaliyot"), {
                "fields": ("professional_practice_time", "course_work_time")
            }
        ),
        (
            _("Asosiy"), {
                "fields": ("direction", "study_semestr")
            }
        )
    )
admin.site.register(StudyPlan, StudyPlanAdmin)
from django.contrib import admin
from exercises.models import Exercise
from exercises.models import Discipline

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'exo_number', 'question')
    ordering = ('discipline', 'exo_number', )
    list_filter = ('discipline', 'exo_number', )


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Discipline)


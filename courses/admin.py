from django.contrib import admin
from courses.models import Course , Topic,CourseGroup,Lesson,Activity


# Add in this class to customized the Admin Interface
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registeration to include this customised interface
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic)
admin.site.register(CourseGroup)
admin.site.register(Lesson)
admin.site.register(Activity)


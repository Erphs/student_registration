from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Student, Course, Enrollment


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student



@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ('title', 'created_at')
    search_fields = ('title', )

class EnrollmentResource(resources.ModelResource):
    class Meta:
        model = Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(ImportExportModelAdmin):
    resource_classes = EnrollmentResource
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('course', )


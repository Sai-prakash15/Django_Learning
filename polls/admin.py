from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        (None, {'fields': ['id']}),
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['opened']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

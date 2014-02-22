from django.contrib import admin
from sven.app.quiz.models import Category, Question, Answer
from django.core.urlresolvers import reverse
class AnswerAdmin(admin.StackedInline):
	model = Answer
	extra = 0

class QuestionAdmin(admin.ModelAdmin):

	def category(obj):
		url = reverse('admin:%s_%s_change' %(obj.category._meta.app_label,  obj.category._meta.module_name),  args=[obj.category.id] )
  		return u'<a href="%s">%s</a>' %(url,  obj.category)

	category.allow_tags = True

	fieldsets = [
	('Category', {'fields': ['category']}),
	('Question', {'fields': ['text', 'image']}),
	]
	list_display = ('text', category)
	search_fields = ['text']
	inlines = [AnswerAdmin]



admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
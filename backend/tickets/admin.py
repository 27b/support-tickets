from django.contrib import admin

from .models import Ticket, Comment


admin.site.site_title = 'Support Tickets'
admin.site.site_header = 'Support Tickets'
admin.site.index_title = 'Support Tickets'


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('user', 'content', 'created_at')
    can_delete = False
    extra = 0
    max_num = 0
    verbose_name = 'comment'
    verbose_name_plural = 'Comments'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content']


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    inlines = [CommentInline]


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
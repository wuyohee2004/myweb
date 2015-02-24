from django.contrib import admin
from poll.models import *

class OpsLogAdmin(admin.ModelAdmin):
    list_display = ('log_type','finish_date','log_type','poll_user','run_user','cmd'
                    ,'total_task','success_num','failed_num','track_mark','note')

class LogAdmin(admin.ModelAdmin):
    list_display = ('user','ip','event_type','cmd','event_log','result','track_mark')

admin.site.register(IP)
admin.site.register(Group)
admin.site.register(RemoteUser)
admin.site.register(PollUser)
admin.site.register(AuthByIpAndRemoteUser)
admin.site.register(OpsLog,OpsLogAdmin)
admin.site.register(OpsLogTemp,LogAdmin)




# class Author_Admin(admin.ModelAdmin):
#     list_display = ('last_name','first_name','email')
#     search_fields = ('first_name', 'last_name')
#
# class Book_Admin(admin.ModelAdmin):
#     list_display = ('title','publisher','publication_date',)
#     filter_horizontal = ('authors',)
#     list_filter = ('publication_date','publisher','title')
#     search_fields = ('title',)
#
# admin.site.register(Publisher)
# admin.site.register(Author,Author_Admin)
# admin.site.register(Book,Book_Admin)

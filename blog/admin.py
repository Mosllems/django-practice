from django.contrib import admin

from .models import Post, Category



class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'status', 'datetime_created')
    List_select_related = ('author', )
    list_filter = ('author__username', )
    list_per_page = 10
    search_fields = ('author__username', 'title')

    def get_first_name(self, obj):
        return obj.author.first_name
    get_first_name.short_description = "First Name"



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    list_per_page = 10
    search_fields = ('name',)    

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)

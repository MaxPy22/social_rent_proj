from django.contrib import admin
from .models import Category, Type, EquipmentModel, EquipmentUnit, EquipmentModelComment


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category_title', )


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_title', 'get_models_count', )
    list_display_links = ('type_title', )
    search_fields = ('type_title', ) #, 'category', )

class EquipmentUnitInline(admin.TabularInline):
    model = EquipmentUnit
    can_delete = False
    extra = 0


class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name', 'description', 'type', 'show_categories', )
    list_filter = ('type', 'category', ) # , 'show_categories', )
    inlines = (EquipmentUnitInline, )


class EquipmentUnitAdmin(admin.ModelAdmin):
    list_display = ('equipment_model', 'id', 'status', 'returning_date', 'notes', 'patient')
    list_filter = ('status','returning_date', )
    search_fields = ('equipment_model__model_name', 'patient__username' )
    readonly_fields = ('id', )
    list_editable = ('status', 'returning_date', )  # leidzia redaguoti isrinktus laukus prie bendro elementu saraso

    fieldsets = (
        ('Pagrindinė Informacija', {'fields': (
                # 'id', 
                'equipment_model',
                ('status', 'returning_date', )
            )}),
        ('Kita informacija', {'fields': (
                ('patient', 'notes',)
            )}),
)


admin.site.register(Category)
admin.site.register(Type, TypeAdmin)
admin.site.register(EquipmentModel, EquipmentModelAdmin)
admin.site.register(EquipmentUnit, EquipmentUnitAdmin)
admin.site.register(EquipmentModelComment)

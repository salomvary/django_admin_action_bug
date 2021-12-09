from django.contrib import admin
from django.db.models import Value, Count

from my_app.models import Thing


@admin.action(description="Update something")
def update_something(admin, request, queryset):
    queryset.update(is_something=True)


class ThingAdmin(admin.ModelAdmin):
    actions = [update_something]

    list_display = (
        "__str__",
        "other_things_count",
    )

    @admin.display(description="Other things count")
    def other_things_count(self, obj):
        return obj.other_things_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        queryset = queryset.annotate(
            other_things_count=Count("other_things"),
        ).order_by("other_things_count")

        return queryset


admin.site.register(Thing, ThingAdmin)

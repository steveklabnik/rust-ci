from django.contrib import admin
from ppatrigger.models import Ppa, Package, Project, ProjectDocs, ProjectCategory

admin.site.register(Ppa)
admin.site.register(Package)
admin.site.register(Project)
admin.site.register(ProjectDocs)
admin.site.register(ProjectCategory)


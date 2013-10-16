import traceback
from django.core.management.base import BaseCommand
from ppatrigger.models import Project
from travis_client import get_build_by_id
import json

# For debugging Travis responses
class Command(BaseCommand):
    args = '<project_id project_id ...>'
    help = 'Fetch data for last build of a project and print it'

    def handle(self, *args, **options):

        if len(args) == 0:
            raise CommandError('Provide at least one numeric project id')

        for project_id in args:
            project = Projects.objects.get(pk = project_id)

            build = get_build_by_id(project.build_id)

            self.stdout.write(json.dumps(build, sort_keys=True, indent=4))


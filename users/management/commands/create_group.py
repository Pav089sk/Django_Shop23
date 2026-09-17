from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, ContentType, Permission
from catalog.models import Product


class Command(BaseCommand):
    help = 'Create group "moderators"'

    def handle(self, *args, **kwargs):
        editors_group, created = Group.objects.get_or_create(name='moderators')
        ct = ContentType.objects.get_for_model(Product)
        canceled_permission = Permission.objects.get(content_type = ct, codename='can_unpublish_product')
        deleted_permission = Permission.objects.get(content_type = ct, codename='delete_product')
        editors_group.permissions.add(canceled_permission, deleted_permission)
        self.stdout.write(self.style.SUCCESS('Created group "moderators"'))


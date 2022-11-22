from blog.models import Category, Tag
from django.core.management.base import BaseCommand


# TODO 参数化
class Command(BaseCommand):
    help = "build search words"

    def handle(self, *args, **options):
        datas = set(
            [t.name for t in Tag.objects.all()]
            + [t.name for t in Category.objects.all()]
        )
        print("\n".join(datas))

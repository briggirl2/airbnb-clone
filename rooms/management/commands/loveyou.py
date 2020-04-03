from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command tells me that he loves me."

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
            # SUCCESS, ERROR, WARNING 별로 터미널에 출력되는 색 다름 색 다름

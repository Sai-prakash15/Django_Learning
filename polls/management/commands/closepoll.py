from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = 'Closes the specified poll for voting '

    def add_arguments(self, parser):
        # positional arguments
        parser.add_argument('poll_ids', nargs='+', type=int)

        # Named arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)
            if options['delete']:
                poll.delete()
                self.stdout.write(self.style.SUCCESS('Successfully deleted poll "%s"' % poll_id))
            else:
                if (poll.opened == False):
                    self.stdout.write(self.style.ERROR('"%s" poll is already closed' % poll_id))
                else:
                    poll.opened = False
                    poll.save()
                    self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

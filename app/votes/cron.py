from django_cron import CronJobBase, Schedule
from posts.models import Post;
from votes.models import Vote;


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'votes.cron.MyCronJob'

    def do(self):
        Vote.objects.all().delete()
        Post.objects.all().update(upvotes=0);

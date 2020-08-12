from posts.models import Post
from votes.models import Vote
from celery.task import periodic_task
from datetime import timedelta
import os

VOTES_RESET_TIMEDELTA = os.getenv("VOTES_RESET_TIMEDELTA")


@periodic_task(run_every=timedelta(minutes=int(VOTES_RESET_TIMEDELTA)),
               name='reset_votes')
def reset_votes():
    print("Votes've just reseted!")
    Vote.objects.all().delete()
    Post.objects.all().update(upvotes=0)

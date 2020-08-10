python3  /app/manage.py shell --command="from posts.models import Post; Post.objects.all().update(upvotes=0); from votes.models import Vote; Vote.objects.all().delete()"

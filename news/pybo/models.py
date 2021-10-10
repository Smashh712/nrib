from django.db import models

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    side = models.NullBooleanField()

    def __str__(self):
        return self.subject


class Issue(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    moderator = models.CharField(max_length=200)
    agree = models.CharField(max_length=200)
    disagree = models.CharField(max_length=200)

    agree_representor = models.CharField(max_length=20, null=True, default="")
    agree_representor_id = models.CharField(max_length=20, null=True, default="")
    agree_represent = models.TextField(null=True, default="")
    disagree_representor = models.CharField(max_length=20, null=True, default="")
    disagree_representor_id = models.CharField(max_length=20, null=True, default="")
    disagree_represent = models.TextField(null=True, default="")

    youtube = models.CharField(max_length=50, null=True, default="")

    def __str__(self):
        return self.subject


class Issue_reply(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    like = models.PositiveIntegerField(default=0)
    side = models.NullBooleanField()

    def __str__(self):
        return self.content


class Issue_rereply(models.Model):
    issue_reply = models.ForeignKey(Issue_reply, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content

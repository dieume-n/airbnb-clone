from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Conversation Model definition """
    participants = models.ManyToManyField('users.User', blank=True)

    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

    count_messages.short_description = "# of Messages"
    count_participants.short_description = "# of Participants"

    def __str__(self):
        usernames = [user.username for user in self.participants.all()]
        return ', '.join(usernames)


class Message(core_models.TimeStampedModel):
    """ Message Model definition """
    message = models.TextField()
    user = models.ForeignKey('users.User', related_name='messages', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.message}'

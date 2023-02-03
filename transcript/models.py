from django.db import models

class WikiSearch(models.Model):
    result= models.JSONField(name='result')
    text = models.TextField(name = 'text')

class GPTSearch(models.Model):
    answer = models.JSONField(name ="answer")
    text = models.TextField(name = 'text')

class TranscriptInteract(models.Model):
    text = models.TextField(name = 'text')
    gpt_answer = models.JSONField(name ="gpt_answer")
    wiki_result = models.JSONField(name='wiki_result')
    google_result = models.JSONField(name='google_result')



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Dev(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False, verbose_name="Seu nome")
    job = models.CharField(max_length=250, blank=False, null=False, default="Dev", verbose_name="Seu cargo anterior")
    place = models.CharField(max_length=200, blank=False, null=False, verbose_name="Localidade que você se encontra")
    email = models.EmailField(blank=False, null=False, verbose_name="Seu e-mail")
    github = models.URLField(blank=True, null=True, verbose_name="Seu Github, se tiver")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Seu Linkedin, se tiver")

    @property
    def short_linkedin_url(self):
        if self.linkedin is None:
            return ""
        return str(self.linkedin).split('/in/')[1]

    @property
    def short_github_url(self):
        if self.github is None:
            return ""
        return str(self.github).split('.com/')[1]
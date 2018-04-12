# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 23:21
from __future__ import unicode_literals

from django.db import migrations


def populate_label_field(apps, schema_editor):
    SpatialUnit = apps.get_model('spatial', 'SpatialUnit')
    QuestionOption = apps.get_model('questionnaires', 'QuestionOption')
    question_options = QuestionOption.objects.filter(
        question__name='location_type').select_related('question')
    for qo in question_options:
        SpatialUnit.objects.filter(
            type=qo.name,
            project__current_questionnaire=qo.question.questionnaire_id,
        ).update(label=qo.label_xlat)


class Migration(migrations.Migration):

    dependencies = [
        ('spatial', '0011_add_label_field'),
    ]

    operations = [
        migrations.RunPython(
            populate_label_field,
            reverse_code=migrations.RunPython.noop
        ),
    ]
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'quiz_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'quiz', ['Category'])

        # Adding model 'Question'
        db.create_table(u'quiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Category'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'quiz', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'quiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'quiz', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'quiz_category')

        # Deleting model 'Question'
        db.delete_table(u'quiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'quiz_answer')


    models = {
        u'quiz.answer': {
            'Meta': {'object_name': 'Answer'},
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'quiz.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'quiz.question': {
            'Meta': {'object_name': 'Question'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quiz']
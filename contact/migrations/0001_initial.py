# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationType'
        db.create_table(u'contact_locationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'contact', ['LocationType'])

        # Adding model 'WebSite'
        db.create_table(u'contact_website', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=128)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='websites', null=True, to=orm['contact.LocationType'])),
        ))
        db.send_create_signal(u'contact', ['WebSite'])

        # Adding model 'Phone'
        db.create_table(u'contact_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='phones', null=True, to=orm['contact.LocationType'])),
        ))
        db.send_create_signal(u'contact', ['Phone'])

        # Adding model 'Address'
        db.create_table(u'contact_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact.LocationType'], null=True, blank=True)),
        ))
        db.send_create_signal(u'contact', ['Address'])

        # Adding model 'Email'
        db.create_table(u'contact_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='emails', null=True, to=orm['contact.LocationType'])),
        ))
        db.send_create_signal(u'contact', ['Email'])

        # Adding model 'Date'
        db.create_table(u'contact_date', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'contact', ['Date'])

        # Adding model 'CustomData'
        db.create_table(u'contact_customdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=192)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='custom_data', null=True, to=orm['contact.LocationType'])),
        ))
        db.send_create_signal(u'contact', ['CustomData'])

        # Adding model 'IdentityData'
        db.create_table(u'contact_identitydata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'contact', ['IdentityData'])

        # Adding model 'Identity'
        db.create_table(u'contact_identity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'contact', ['Identity'])

        # Adding M2M table for field field_data on 'Identity'
        m2m_table_name = db.shorten_name(u'contact_identity_field_data')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('identity', models.ForeignKey(orm[u'contact.identity'], null=False)),
            ('identitydata', models.ForeignKey(orm[u'contact.identitydata'], null=False))
        ))
        db.create_unique(m2m_table_name, ['identity_id', 'identitydata_id'])

        # Adding model 'Person'
        db.create_table(u'contact_person', (
            (u'identity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contact.Identity'], unique=True, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'contact', ['Person'])

        # Adding model 'Company'
        db.create_table(u'contact_company', (
            (u'identity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contact.Identity'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'contact', ['Company'])

        # Adding model 'Group'
        db.create_table(u'contact_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'contact', ['Group'])

        # Adding M2M table for field members on 'Group'
        m2m_table_name = db.shorten_name(u'contact_group_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'contact.group'], null=False)),
            ('identity', models.ForeignKey(orm[u'contact.identity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'identity_id'])


    def backwards(self, orm):
        # Deleting model 'LocationType'
        db.delete_table(u'contact_locationtype')

        # Deleting model 'WebSite'
        db.delete_table(u'contact_website')

        # Deleting model 'Phone'
        db.delete_table(u'contact_phone')

        # Deleting model 'Address'
        db.delete_table(u'contact_address')

        # Deleting model 'Email'
        db.delete_table(u'contact_email')

        # Deleting model 'Date'
        db.delete_table(u'contact_date')

        # Deleting model 'CustomData'
        db.delete_table(u'contact_customdata')

        # Deleting model 'IdentityData'
        db.delete_table(u'contact_identitydata')

        # Deleting model 'Identity'
        db.delete_table(u'contact_identity')

        # Removing M2M table for field field_data on 'Identity'
        db.delete_table(db.shorten_name(u'contact_identity_field_data'))

        # Deleting model 'Person'
        db.delete_table(u'contact_person')

        # Deleting model 'Company'
        db.delete_table(u'contact_company')

        # Deleting model 'Group'
        db.delete_table(u'contact_group')

        # Removing M2M table for field members on 'Group'
        db.delete_table(db.shorten_name(u'contact_group_members'))


    models = {
        u'contact.address': {
            'Meta': {'object_name': 'Address'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contact.LocationType']", 'null': 'True', 'blank': 'True'})
        },
        u'contact.company': {
            'Meta': {'object_name': 'Company', '_ormbases': [u'contact.Identity']},
            u'identity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contact.Identity']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'contact.customdata': {
            'Meta': {'object_name': 'CustomData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'custom_data'", 'null': 'True', 'to': u"orm['contact.LocationType']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '192'})
        },
        u'contact.date': {
            'Meta': {'object_name': 'Date'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'contact.email': {
            'Meta': {'object_name': 'Email'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'emails'", 'null': 'True', 'to': u"orm['contact.LocationType']"})
        },
        u'contact.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contact.Identity']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'contact.identity': {
            'Meta': {'object_name': 'Identity'},
            'field_data': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'identity'", 'blank': 'True', 'to': u"orm['contact.IdentityData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contact.identitydata': {
            'Meta': {'object_name': 'IdentityData'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'contact.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'contact.person': {
            'Meta': {'object_name': 'Person', '_ormbases': [u'contact.Identity']},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'identity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['contact.Identity']", 'unique': 'True', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'contact.phone': {
            'Meta': {'object_name': 'Phone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'phones'", 'null': 'True', 'to': u"orm['contact.LocationType']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '17'})
        },
        u'contact.website': {
            'Meta': {'object_name': 'WebSite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'websites'", 'null': 'True', 'to': u"orm['contact.LocationType']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '128'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contact']
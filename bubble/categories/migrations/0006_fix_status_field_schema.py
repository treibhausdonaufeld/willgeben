# Generated by Django 5.1.4 on 2025-01-07 11:33

from django.db import migrations


def fix_status_field_schema(apps, schema_editor):
    ItemCategory = apps.get_model('categories', 'ItemCategory')
    
    # Find the "Sachen" category and fix its status field schema
    try:
        sachen_category = ItemCategory.objects.get(name='Sachen', parent_category=None)
        
        # Update the required_fields to remove db_field reference
        if 'status' in sachen_category.required_fields:
            sachen_category.required_fields['status'] = {
                'type': 'choice',
                'choices': ['new', 'used', 'old'],
                'label': 'Zustand'
            }
            sachen_category.save()
            
    except ItemCategory.DoesNotExist:
        pass


def reverse_fix_status_field_schema(apps, schema_editor):
    ItemCategory = apps.get_model('categories', 'ItemCategory')
    
    # Revert back to including db_field
    try:
        sachen_category = ItemCategory.objects.get(name='Sachen', parent_category=None)
        
        if 'status' in sachen_category.required_fields:
            sachen_category.required_fields['status'] = {
                'type': 'choice',
                'choices': ['new', 'used', 'old'],
                'label': 'Zustand',
                'db_field': 'status'
            }
            sachen_category.save()
            
    except ItemCategory.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_remove_content_type_field'),
    ]

    operations = [
        migrations.RunPython(fix_status_field_schema, reverse_fix_status_field_schema),
    ]
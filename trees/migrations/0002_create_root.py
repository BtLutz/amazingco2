from django.db import migrations


def create_root(apps, schema_editor):
    TreeNode = apps.get_model('trees', 'TreeNode')
    TreeNode.objects.create(is_root=True)


class Migration(migrations.Migration):
    dependencies = [('trees', '0001_initial')]
    operations = [migrations.RunPython(create_root)]

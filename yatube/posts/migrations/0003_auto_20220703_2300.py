# Generated by Django 2.2.16 on 2022-07-03 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20220703_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliked_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='posts.Post')),
            ],
            options={
                'verbose_name': 'Dislikes',
                'verbose_name_plural': 'Dislikes',
            },
        ),
        migrations.AddConstraint(
            model_name='dislike',
            constraint=models.UniqueConstraint(fields=('post', 'disliked_user'), name='unique post-disliked_user pair'),
        ),
    ]
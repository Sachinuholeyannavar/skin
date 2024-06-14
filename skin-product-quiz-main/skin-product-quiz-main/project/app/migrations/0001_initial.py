# Generated by Django 5.0.6 on 2024-06-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('skin_care_hair_care', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('teens', models.BooleanField(blank=True, null=True)),
                ('twenties', models.BooleanField(blank=True, null=True)),
                ('thirties', models.BooleanField(blank=True, null=True)),
                ('forties', models.BooleanField(blank=True, null=True)),
                ('fifties', models.BooleanField(blank=True, null=True)),
                ('sixties', models.BooleanField(blank=True, null=True)),
                ('skin_type_normal', models.BooleanField(blank=True, null=True)),
                ('oily', models.BooleanField(blank=True, null=True)),
                ('dry', models.BooleanField(blank=True, null=True)),
                ('sensitive', models.BooleanField(blank=True, null=True)),
                ('combination', models.BooleanField(blank=True, null=True)),
                ('skin_concerns_acne', models.BooleanField(blank=True, null=True)),
                ('aging', models.BooleanField(blank=True, null=True)),
                ('dull_skin', models.BooleanField(blank=True, null=True)),
                ('elasticity', models.BooleanField(blank=True, null=True)),
                ('hydration', models.BooleanField(blank=True, null=True)),
                ('pigmentation', models.BooleanField(blank=True, null=True)),
                ('pores', models.BooleanField(blank=True, null=True)),
                ('redness', models.BooleanField(blank=True, null=True)),
                ('scarring', models.BooleanField(blank=True, null=True)),
                ('sensitive_skin', models.BooleanField(blank=True, null=True)),
                ('sun_protection', models.BooleanField(blank=True, null=True)),
                ('texture', models.BooleanField(blank=True, null=True)),
                ('uneven_skin_tone', models.BooleanField(blank=True, null=True)),
                ('body_care', models.BooleanField(blank=True, null=True)),
                ('eye_cream', models.BooleanField(blank=True, null=True)),
                ('cleanser', models.BooleanField(blank=True, null=True)),
                ('exfoliant', models.BooleanField(blank=True, null=True)),
                ('microneedling', models.BooleanField(blank=True, null=True)),
                ('moisturizer', models.BooleanField(blank=True, null=True)),
                ('peels', models.BooleanField(blank=True, null=True)),
                ('serums', models.BooleanField(blank=True, null=True)),
                ('sun_screen', models.BooleanField(blank=True, null=True)),
                ('spot_treatment', models.BooleanField(blank=True, null=True)),
                ('toner', models.BooleanField(blank=True, null=True)),
                ('use_sunscreen_daily', models.BooleanField(blank=True, null=True)),
                ('react_to_sun_exposure', models.BooleanField(blank=True, null=True)),
                ('hair_loss', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
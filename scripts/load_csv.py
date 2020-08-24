import csv
import os
from glob import iglob

from django.conf import settings

from source.models import GaiaSource


def load_gaia_source_csv(file):
    with open(file) as f:
        csv_file = csv.DictReader(f)
        for obj in csv_file:
            obj_updated = {}
            for key, value in obj.items():
                if value in ['false', 'true']:
                    obj_updated[key] = True if value == 'true' else False
                    continue
                if value == '':
                    value = None
                obj_updated[key] = value
            GaiaSource.objects.get_or_create(**obj_updated)


def run():
    files = iglob(os.path.join(settings.GAIA_SOURCE_PATH, '*.csv'))
    for file in files:
        load_gaia_source_csv(file)


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_stores.Config'


class Default(object):

    apps = [
        'leonardo_stores',
        'stores',
    ]

    plugins = [
        ('eshop_stores.apps.stores', _('Stores'), ),
    ]

    config = {
        'STORES_GEOGRAPHIC_SRID': (3577, _('This is used for distance calculations. See http://spatialreference.org for more details.')),
        'STORES_GEODETIC_SRID': (4326, _('Paypal API Password')),
        'STORES_MAX_SEARCH_DISTANCE': (None, _('This filters stores in queries by distance. Units can be set using distance object')),
    }


class Config(AppConfig, Default):
    name = 'leonardo_stores'
    verbose_name = "Stores"

default = Default()

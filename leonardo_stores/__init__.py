
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_stores.Config'


class Default(object):

    apps = [
        'leonardo_stores',
        'stores',
        'django.contrib.gis',
    ]

    plugins = [
        ('leonardo_stores.apps.stores', _('Stores'), ),
    ]

    config = {
        'STORES_GEOGRAPHIC_SRID': (3577, _('This is used for distance calculations. See http://spatialreference.org for more details.')),
        'STORES_GEODETIC_SRID': (4326, _('Paypal API Password')),
        'STORES_MAX_SEARCH_DISTANCE': (None, _('This filters stores in queries by distance. Units can be set using distance object')),
    }

    css_files = [
        'stores/css/stores.css',
    ]

    js_files = [
        'stores/js/stores.js',
    ]

    absolute_url_overrides = {
        'stores.store': 'leonardo_stores.overrides.store',
    }

    navigation_extensions = [
        'leonardo_stores.navigations.all'
    ]


class Config(AppConfig, Default):
    name = 'leonardo_stores'
    verbose_name = "Stores"

default = Default()


from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from feincms.module.page.extensions.navigation import (
    NavigationExtension, PagePretender)


class StoresNavigationExtension(NavigationExtension):

    """
    Navigation extension for Leonardo Stores
    which lists all available stores
    """

    name = _('List of Stores')

    def children(self, page, **kwargs):
        from oscar.core.loading import get_class

        Store = get_class('stores.models', 'Store')
        stores = Store.objects.all()
        for store in stores:
            yield PagePretender(
                title=store.name,
                url=store.get_absolute_url(),
                tree_id=page.tree_id,
                level=page.level + 1,
                language=getattr(page, 'language', settings.LANGUAGE_CODE),
                slug=store.slug,
                parent=page,
                parent_id=page.id,
                lft=page.lft,
                rght=page.rght,
                _mptt_meta=getattr(page, '_mptt_meta', None),
            )

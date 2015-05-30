
def store(self):
    from leonardo.module.web.widget.application.reverse import app_reverse
    return app_reverse(
        'detail',
        'leonardo_stores.apps.stores',
        kwargs={'dummyslug': self.slug, 'pk': self.pk})

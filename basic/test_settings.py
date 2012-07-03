import os
DIRNAME = os.path.dirname(__file__)

DEFAULT_CHARSET = 'utf-8'

test_engine = os.environ.get("BASIC_TEST_ENGINE", "sqlite3")

DATABASE_ENGINE = test_engine
DATABASE_NAME = os.environ.get("BASIC_DATABASE_NAME", "tagging_test")
DATABASE_USER = os.environ.get("BASIC_DATABASE_USER", "")
DATABASE_PASSWORD = os.environ.get("BASIC_DATABASE_PASSWORD", "")
DATABASE_HOST = os.environ.get("BASIC_DATABASE_HOST", "localhost")

if test_engine == "sqlite":
    DATABASE_NAME = os.path.join(DIRNAME, 'basic_test.db')
    DATABASE_HOST = ""
elif test_engine == "mysql":
    DATABASE_PORT = os.environ.get("BASIC_DATABASE_PORT", 3306)
elif test_engine == "postgresql_psycopg2":
    DATABASE_PORT = os.environ.get("BASIC_DATABASE_PORT", 5432)

SITE_ID=1

# Test suite needs some templates to be loadable, but we don't provide them.
# Empty string works well enough for tests to pass
from django.template import loader, TemplateDoesNotExist
class myloader(loader.BaseLoader):
    is_usable = True
    def load_template_source(self, template_name, template_dirs=None):
        if template_name in ['registration/registration_form.html', 'invitations/invitation_subject.txt', 'invitations/invitation_message.txt', '404.html']:
            return "", template_name
        else:
            raise TemplateDoesNotExist, template_name

TEMPLATE_LOADERS= (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'test_settings.myloader',
)

ROOT_URLCONF='basic.test_urls'

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.markup',
    'basic.messages',
    'basic.tools',
    'basic.inlines',
    'basic.bookmarks',
    'basic.profiles',
    'basic.media',
    'basic.music',
    'basic.blog',
    'basic.relationships',
    'basic.invitations',
    'basic.flagging',
    'basic.events',
    'basic.comments',
    'basic.groups',
    'basic.movies',
    'basic.places',
    'basic.books',
    'basic.people',
    'tagging',
)

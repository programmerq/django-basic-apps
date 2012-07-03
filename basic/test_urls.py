from django.conf.urls.defaults import patterns, include


urlpatterns = patterns(
    (r'blog/', include('basic.blog.urls')),
    (r'bookmarks/', include('basic.bookmarks.urls')),
    (r'books/', include('basic.books.urls')),
    (r'comments/', include('basic.comments.urls')),
    (r'events/', include('basic.events.urls')),
    (r'flagging/', include('basic.flagging.urls')),
    (r'groups/', include('basic.groups.urls', namespace='groups')),
    #(r'inlines/', include('basic.inlines.urls')),
    (r'invitations/', include('basic.invitations.urls',
                              namespace='invitations')),
    (r'photos/', include('basic.media.urls.photos')),
    (r'videos/', include('basic.media.urls.videos')),
    (r'messages/', include('basic.messages.urls', namespace='messages')),
    (r'movies/', include('basic.movies.urls')),
    (r'music/', include('basic.music.urls')),
    (r'people/', include('basic.people.urls')),
    (r'places/', include('basic.places.urls')),
    (r'profiles/', include('basic.profiles.urls')),
    (r'relationships/', include('basic.relationships.urls')),
    #(r'tools/', include('basic.tools.urls')),
    (r'auth/', include('django.contrib.auth.urls')),
)

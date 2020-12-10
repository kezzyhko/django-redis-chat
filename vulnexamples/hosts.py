from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host('', 'www.urls', name='default'),
)

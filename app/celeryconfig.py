_password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'
_url = 'localhost:6379'

broker_url = f'redis://:{_password}@{_url}/0'
result_backend = f'redis://:{_password}@{_url}/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['application/json']
timezone = 'MSK'
enable_utc = True
# task_annotations =
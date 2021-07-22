password = 'wX4do7Xscne6KJFSD7Shu3xJx3Pn2MxC1JJaQVaVzpxePC'

broker_url = f'redis://:{password}@localhost:6379/0'
result_backend = f'redis://:{password}@localhost:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

def read_config_file(file_path):
    with open(file=file_path, mode='r') as fs:
        return {k.strip(): v.strip() for i in [l for l in fs.readlines() if l.strip() != ''] for k, v in [i.split('=')]}


print('file as dic: ', read_config_file('config.properties'))

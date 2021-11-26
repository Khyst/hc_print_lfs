import os

def rename_imagefile_to_uuid(instance, filename):
    upload_to = f'{instance.prefix}'
    print(instance)

    if instance: # 인스턴스가 존재하면
        ext = filename.split('.')[-1]
        filename = '{}_{}.{}'.format(instance.prefsix.split('/')[-2], instance.id, ext)
        instance_name = '{}'.format(instance.prefix.split('/')[-1])

    return os.path.join(upload_to, filename)
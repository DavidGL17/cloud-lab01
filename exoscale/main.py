import exoscale
from time import sleep


def createInstance(exo,name, zone):
    # Setup ip and zone
    print(f'Creating instance {name} in {zone.name}')
    instance = exo.compute.create_instance(
        name=name,
        zone=zone,
        type=exo.compute.get_instance_type("medium"),
        template=list(
            exo.compute.list_instance_templates(
                zone,
                "Linux Ubuntu 20.04 LTS 64-bit"))[0],
        volume_size=50,
        security_groups=[]
    )
    
def instancesStatus(exo, zone):
    print('Instances status:')
    for instance in exo.compute.list_instances(zone):
        print("{name} {zone} {ip}".format(
            name=instance.name,
            zone=instance.zone.name,
            ip=instance.ipv4_address,
        ))  
    print(f'Buckets status:')
    for bucket in exo.storage.list_buckets():
        print(bucket.name)

def createBucket(exo, name, zone):
    backups_bucket = exo.storage.create_bucket(name=name, zone="ch-gva-2")

def deleteAllInstance(exo,zone):
    print(f'Deleting all instances in {zone.name}')
    for instance in exo.compute.list_instances(zone):
        print(f'Deleting {instance.name} in {zone.name} with ip {instance.ipv4_address}')
        instance.delete()

def deleteAllBucket(exo):
    for bucket in exo.storage.list_buckets():
        print(f'Deleting {bucket.name}')
        bucket.delete()

def main():
    # Create exoscale api object
    exo = exoscale.Exoscale(config_file='/home/david/.exoscale/config.tml')
    zone_gva2 = exo.compute.get_zone("ch-gva-2")

    createBucket(exo, 'testdavid', zone_gva2)
    createInstance(exo,"test", zone_gva2)
    instancesStatus(exo, zone_gva2)
    sleep(10)
    deleteAllInstance(exo, zone_gva2)
    deleteAllBucket(exo)
    instancesStatus(exo,zone_gva2)

if __name__ == '__main__':
    main()
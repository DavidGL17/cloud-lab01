import gceFunctions as gce
from time import sleep

projectId = 'cloudlab01-363806'
zone = 'europe-west6-a'

def main():
    print('Creating instance...')
    gce.create_from_disk_and_machine_image(projectId, zone, 'test-instance',f'projects/{projectId}/global/images/image-1',f'projects/{projectId}/global/machineImages/tmp1')
    print('Listing instances...')
    gce.list_instances(projectId, zone)
    sleep(5)
    print('Deleting instance...')
    gce.delete_instance(projectId, zone, 'test-instance')

if __name__ == '__main__':
    main()
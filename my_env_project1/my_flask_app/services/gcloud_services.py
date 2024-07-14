from googleapiclient.discovery import build
import google.auth

def create_dataproc_cluster(cluster_name):
    credentials, project = google.auth.default()
    service = build('dataproc', 'v1', credentials=credentials)
    
    cluster_data = {
        'clusterName': cluster_name,
        'config': {
            'gceClusterConfig': {
                'zoneUri': 'us-central1-a'
            },
            'masterConfig': {
                'numInstances': 1,
                'machineTypeUri': 'n1-standard-4'
            },
            'workerConfig': {
                'numInstances': 2,
                'machineTypeUri': 'n1-standard-4'
            }
        }
    }

    result = service.projects().regions().clusters().create(
        projectId=project,
        region='us-central1',
        body=cluster_data).execute()
    
    return result['clusterName']
    
from kubernetes import client, config

def executeAction(args):
    if args.action == "list":
        get(args)
    elif args.action == "create":
        create(args)
    elif args.action == "update":
        update(args)
    elif args.action == "delete":
        delete(args)
    else: 
        "You're too young to party"

def get(args):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    deployments_list = v1.list_namespaced_deployment(namespace=args.namespace)
    deployments = [item.metadata.name for item in deployments_list.items]
    return deployments

def create(args):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    containers = []
    container1 = client.V1Container(name='my-nginx-container', image='nginx')
    containers.append(container1)
    print(containers)
        
    pod_spec = client.V1DeploymentSpec(containers=containers)
    pod_metadata = client.V1ObjectMeta(name='my-pod', namespace='default')

    pod_body = client.V1Deployment(api_version='v1', kind='Pod', metadata=pod_metadata, spec=pod_spec)
        
    v1.create_namespaced_deployment(namespace='default', body=pod_body)

def update(args):
    print ("issue not implemented yet!")

def delete(args):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    # Delete deployment
    resp = v1.delete_namespaced_deployment(
        name=args.name,
        namespace=args.namespace,
        body=client.V1DeleteOptions(
            propagation_policy="Foreground", grace_period_seconds=5
        ),
    )
    print("\n[INFO] deployment" + "`" + args.name + "`" + " deleted.")


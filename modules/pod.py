from kubernetes import client, config
import logging
import sys
import argparse

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
    pods_list = v1.list_namespaced_pod(namespace=args.namespace)
    pods = [item.metadata.name for item in pods_list.items]
    print(pods)

def create(args):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    containers = []
    container1 = client.V1Container(name=args.name, image='nginx')
    containers.append(container1)
        
    pod_spec = client.V1PodSpec(containers=containers)
    pod_metadata = client.V1ObjectMeta(name=args.name, namespace=args.namespace)
    pod_body = client.V1Pod(api_version='v1', kind='Pod', metadata=pod_metadata, spec=pod_spec)
       
    v1.create_namespaced_pod(namespace=args.namespace, body=pod_body)

def update(args):
    print ("issue not implemented yet!")

def delete(args):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    v1.delete_namespaced_pod(namespace='default', name='my-pod')
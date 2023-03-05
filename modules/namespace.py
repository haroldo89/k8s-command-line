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
    namespaces_list = v1.list_namespace()
    namespaces = [item.metadata.name for item in namespaces_list.items]
    return namespaces

def create():
    print("not implemented yet")

def update(args):
    print ("issue not implemented yet!")

def delete(namespaceName,deploymentName):
    print("not implemented yet")
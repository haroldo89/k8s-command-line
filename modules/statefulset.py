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
    print("not implemented yet")

def create(args):
    print("not implemented yet")

def update(args):
    print ("issue not implemented yet!")

def delete(args):
    print("not implemented yet")
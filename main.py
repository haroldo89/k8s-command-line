import argparse
import modules.deployment as deployment
import modules.pod as pod
import modules.statefulset as statefulset
import modules.namespace as namespace


argParser = argparse.ArgumentParser()
argParser.add_argument("-ns", "--namespace", help="name of your namespace",required=True)
argParser.add_argument("-a", "--action", help="action to execute",choices=["create","update","delete","list"],required=True)
argParser.add_argument("-k", "--kind", help="name of kind object",choices=["namespace","deployment","pod","statefulset"],required=True)
argParser.add_argument("-nm", "--name", help="name of object to manage",required=True)

def main():
    args = argParser.parse_args()
    print("args=%s" % args)
    if args.kind == "pod":
        pod.executeAction(args)
    elif args.kind == "deployment":
        deployment.executeAction(args)
    elif args.kind == "statefulset":
        statefulset.executeAction(args)
    elif args.kind == "namespace":
        namespace.executeAction(args)
    else: 
        "Object not supported yet!"
      
if __name__ == '__main__':
    main()
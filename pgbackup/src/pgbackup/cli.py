from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 's3' and 'local'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL of the PostgreSQL database to backup")
    parser.add_argument('--driver', 
        help="how and where to store the backup", 
        nargs=2,
        action=DriverAction,
        required=True)    
    return parser

def main():
    import boto3
    from pgbackup imprt pgdump, storage

    args = create_parser().parser_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3('s3')
        storage.s3_client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)

import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-fn', metavar='NAME', help='Search with full-name')
    parser.add_argument('-ip', metavar='IP_ADDRESS', help='Search with ip address')
    parser.add_argument('-u', action='store_true', help='Search with username')

    # Parse only known arguments, ignore unknown ones
    args, unknown = parser.parse_known_args()

    if unknown:
        print("Unrecognized arguments:", ' '.join(unknown))
        print("OPTIONS:")
        print("    -map         Search with map get lat /")
        print("    -stag         Search with ip address")
       
        sys.exit(1)

    if args.map:
      print("map")
    elif args.steg:
        print("stag")
    else:
        print("No search criteria specified")

if __name__ == "__main__":
    main()

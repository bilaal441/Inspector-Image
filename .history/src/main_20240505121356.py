import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-map', metavar='map', help='Search with full-name')
    parser.add_argument('-stag', metavar='IP_ADDRESS', help='Search with ip address')
   

    # Parse only known arguments, ignore unknown ones
    args, unknown = parser.parse_known_args()

    if unknown:
        print("Unrecognized arguments:", ' '.join(unknown))
        print("OPTIONS:")
        print("    -map         Search with map get lat / lon")
        print("    -stag         Search with  stag  get PUBLIC KEY")
       
        sys.exit(1)

    if args.map:
      print("map")
    elif args.steg:
        print("stag")
    else:
        print("No search criteria specified")

if __name__ == "__main__":
    main()

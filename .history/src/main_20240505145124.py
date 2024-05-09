import sys
import argparse
import pgs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-map', metavar='map', help='Search with image')
    parser.add_argument('-stag', metavar='stag', help='Search with  image')
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
        pgs.

        print("stag")
    else:
        print("No search criteria specified")

if __name__ == "__main__":
    main()

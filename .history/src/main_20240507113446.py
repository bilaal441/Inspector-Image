import sys
import argparse
import pgs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-map', metavar='map', help='Search with map get lat / lon')
    parser.add_argument('-steg', metavar='steg', help='Search with steg get PUBLIC KEY')  # Corrected typo from 'stag' to 'steg'
    args, unknown = parser.parse_known_args()

    if unknown:
        print("Unrecognized arguments:", ' '.join(unknown))
        print("OPTIONS:")
        print("    -map         Search with map get lat / lon")
        print("    -steg        Search with steg get PUBLIC KEY")  # Corrected typo from 'stag' to 'steg'
        sys.exit(1)

    if args.map:
        print("map")
    elif args.steg:
        print(pgs.extract_pgp_key(args.steg))  # Assuming pgs.read_pgp_key() returns the PUBLIC KEY
    else:
        print("No search criteria specified")

if __name__ == "__main__":
    main()

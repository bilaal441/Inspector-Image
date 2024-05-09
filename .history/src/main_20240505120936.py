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
        print("    -fn         Search with full-name")
        print("    -ip         Search with ip address")
        print("    -u          Search with username")
        sys.exit(1)

    if args.fn:
      print()
    elif args.ip:
    
    elif args.u:
        print("Searching with username")
    else:
        print("No search criteria specified")

if __name__ == "__main__":
    main()

import argparse


def main():
    parser = argparse.ArgumentParser(prog="miniql", description="miniql")
    parser.add_argument("-v", "--version", action="store_true")
    args = parser.parse_args()
    if args.version:
        print("miniql v1.0")


if __name__ == "__main__":
    main()

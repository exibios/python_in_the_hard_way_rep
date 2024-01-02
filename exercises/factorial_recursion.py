from argparse import ArgumentParser

def rec(n):
    #print("Hola")
    if n <= 0:
        return "non positive value"
    if n == 0:
        return 1
    return n*rec(n-1)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("stop", type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    print(rec(args.stop))


if __name__ == "__main__":
    main()
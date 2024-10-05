import sys

def main():
    a = sys.stdin.read
    data = a().splitlines()
    n, q = map(int, data[0].split())
    arrows = list(map(int, data[1].split()))
    k = list(map(int, data[2::]))
    for i in k:

        if (max(arrows) + 1) // 2 > i:
            print('0')
        else:
            print(max(arrows) + 1)


if __name__ == "__main__":
    main()


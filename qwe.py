import sys

def main():
    a = sys.stdin.read
    data = a().splitlines()
    n, q = map(int, data[0].split())
    arrows = list(map(int, data[1].split()))
    k = [int(data[i + 2]) for i in range(q)]
    results = []
    for k in k:
        valid_arrows = [arrow for arrow in arrows if arrow > k]
        if not valid_arrows:
            results.append(0)
            continue
        m = min(valid_arrows)
        robin_ar = m + 1
        if robin_ar > 2 * m:
            results.append(0)
        else:
            results.append(robin_ar)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

ййййййййййййййййййййййййй
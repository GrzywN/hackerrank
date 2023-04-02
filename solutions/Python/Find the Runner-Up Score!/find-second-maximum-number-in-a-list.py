if __name__ == '__main__':
    n = int(input())
    set = set(map(int, input().split()))

    max_score = max(set)
    set.remove(max_score)
    runner_up_score = max(set)

    print(runner_up_score)

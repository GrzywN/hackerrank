if __name__ == '__main__':
    name_and_score = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_and_score.append([name, score])

    scores = set([entry[1] for entry in name_and_score])
    lowest_score = min(scores)
    scores.remove(lowest_score)
    second_lowest_score = min(scores)

    second_lowest_score_names = []
    for entry in name_and_score:
        name, score = entry

        if score == second_lowest_score:
            second_lowest_score_names.append(name)

    for name in sorted(second_lowest_score_names):
        print(name)

import sys


def rankings(filename):
    points = {}
    with open(filename, 'r') as f:
        for line in f:
            # break them into teams
            team1 = line.split(',')[0].strip()
            team2 = line.split(',')[-1].strip()

            # get team name and score
            team1_name = team1.strip()[:len(team1) - 1]
            team1_score = team1[-1]

            # add to the dictionary
            if team1_name not in points:
                points[team1_name] = 0

            # get team name and score
            team2_name = team2.strip()[:len(team2) - 1]
            team2_score = team2[-1]

            # add to the dictionary
            if team2_name not in points:
                points[team2_name] = 0

            # update points

            if team1_score > team2_score:
                points[team1_name] += 3
            elif team2_score > team1_score:
                points[team2_name] += 3
            else:
                points[team2_name] += 1
                points[team1_name] += 1

    sorted_rankings = dict(sorted(points.items(), key=lambda x: (-x[1], x[0])))

    return sorted_rankings


def write_to_file():
    get_rankings = rankings(sys.argv[1])

    # write to file

    position = 1  # ranking position
    prev_value = -1

    with open("output.txt", 'w') as f:
        for key, value in get_rankings.items():
            cur_value = value
            if cur_value == prev_value:
                f.write(str(position - 1) + '. ' + key.strip() + ', ' + str(value) + ' pts\n')

            else:
                f.write(str(position) + '. ' + key.strip() + ', ' + str(value) + ' pts\n')

            position += 1
            prev_value = cur_value


if __name__ == '__main__':
    write_to_file()

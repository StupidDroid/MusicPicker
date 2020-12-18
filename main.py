import csv
import random
import operator


def oneToFour(criterion):
    input_value = 0
    while(input_value < 1 or input_value > 4):
        try:
            input_value = int(input("1. Low\n2. Medium \n3. High \n"
                                    "4. Neutral \nPlease input " + criterion +
                                    " (1-4): "))
        except ValueError:
            pass
    return input_value


def meetsCriterion(criterion, song):
    crit_index = criterion[0] + 1
    song_value = int(song[crit_index])
    if(criterion[1] == 1):
        return (song_value <= 5)
    elif(criterion[1] == 2):
        return (song_value >= 4 and song_value <= 8)
    elif(criterion[1] == 3):
        return (song_value >= 6)
    elif(criterion[1] == 4):
        return True


def correlation(criteria, active_song, prosp_song):
    correlation = 0
    correlation += (1.0 * (9 - abs(int(active_song[criteria[0][0] + 1]) -
                    int(prosp_song[criteria[0][0] + 1]))))
    correlation += (0.9 * (9 - abs(int(active_song[criteria[1][0] + 1]) -
                    int(prosp_song[criteria[1][0] + 1]))))
    correlation += (0.75 * (9 - abs(int(active_song[criteria[2][0] + 1]) -
                    int(prosp_song[criteria[2][0] + 1]))))
    correlation += (0.6 * (9 - abs(int(active_song[criteria[3][0] + 1]) -
                    int(prosp_song[criteria[3][0] + 1]))))
    correlation += (0.5 * (9 - abs(int(active_song[criteria[4][0] + 1]) -
                    int(prosp_song[criteria[4][0] + 1]))))
    correlation += (0.3 * (9 - abs(int(active_song[criteria[5][0] + 1]) -
                    int(prosp_song[criteria[5][0] + 1]))))

    if(active_song[8] == prosp_song[8]):
        correlation += 1

    if(active_song[9] == prosp_song[9]):
        correlation += 1

    correlation += (random.randint(-10, 10) / 10)
    correlation = round(correlation, 1)
    return correlation


def songsMatchingCriterion(criterion, pool):
    matched_songs = []
    for song in pool:
        if(meetsCriterion(criterion, song)):
            matched_songs.append(song)

    if(len(matched_songs) > 0):
        return matched_songs
    else:
        return pool


with open('song_db.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    intensity_input = oneToFour("Intensity")
    engagement_input = oneToFour("Engagement")
    theater_input = oneToFour("Theater")
    sappiness_input = oneToFour("Sappiness")
    depression_input = oneToFour("Depression")
    rebellion_input = oneToFour("Rebellion")
    numerical_inputs = [
        (1, intensity_input),
        (2, engagement_input),
        (3, theater_input),
        (4, sappiness_input),
        (5, depression_input),
        (6, rebellion_input)
    ]

    important_index = 0
    while(important_index < 1 or important_index > 6):
        try:
            important_index = int(input("1. Intensity \n2. Engagement \n"
                                        "3. Theater \n4. Sappinness \n"
                                        "5. Depression \n6. Rebellion \n"
                                        "Pick predominant criterion (1-6): "))
        except ValueError:
            pass
    important_index -= 1

    sorted_criteria = []
    sorted_criteria.append(numerical_inputs.pop(important_index))

    non_surprise_criteria = []
    for i in range(0, len(numerical_inputs)):
        if(numerical_inputs[i][1] != 4):
            non_surprise_criteria.append(numerical_inputs[i])

    for i in range(0, len(non_surprise_criteria)):
        sorted_criteria.append(non_surprise_criteria.pop
                               (random.randint(0, len
                                               (non_surprise_criteria) - 1)))

    surprise_criteria = []
    for i in range(0, len(numerical_inputs)):
        if(numerical_inputs[i][1] == 4):
            surprise_criteria.append(numerical_inputs[i])

    for i in range(0, len(surprise_criteria)):
        sorted_criteria.append(surprise_criteria.pop
                               (random.randint(0, len(surprise_criteria) - 1)))

    next(readCSV)
    song_pool = []
    for song in readCSV:
        if(meetsCriterion(sorted_criteria[0], song)
           and meetsCriterion(sorted_criteria[1], song)):
            song_pool.append(song)

    ordered_playlist = []
    possible_first_songs = song_pool
    for criterion in sorted_criteria:
        possible_first_songs = songsMatchingCriterion(criterion,
                                                      possible_first_songs)
        if(len(possible_first_songs) == 1):
            break
    first_song_index = song_pool.index(possible_first_songs[random.randint
                                       (0, len(possible_first_songs) - 1)])
    ordered_playlist.append(song_pool.pop(first_song_index))

    while(len(song_pool) > 0):
        song_correlations = {}
        for i in range(0, len(song_pool)):
            corr = correlation(sorted_criteria,
                               ordered_playlist[-1], song_pool[i])
            song_correlations[i] = corr
        next_song_index = max(song_correlations.items(),
                              key=operator.itemgetter(1))[0]
        ordered_playlist.append(song_pool.pop(next_song_index))

    for song in ordered_playlist:
        print(song[0])

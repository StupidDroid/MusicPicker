import csv


def oneToFour(criterion):
    input_value = 0
    while(input_value < 1 or input_value > 4):
        try:
            input_value = int(input("1. Low\n2. Medium \n3. High \n"
                                    "4. Surprise \nPlease input " + criterion +
                                    " (1-4): "))
        except ValueError:
            pass
    return input_value


with open('song_db.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    intensity_input = oneToFour("Intensity")
    engagement_input = oneToFour("Engagement")
    theater_input = oneToFour("Theater")
    sappiness_input = oneToFour("Sappiness")
    depression_input = oneToFour("Depression")
    rebellion_input = oneToFour("Rebellion")
    numerical_inputs = [
        ("Intensity", intensity_input),
        ("Engagement", engagement_input),
        ("Theater", theater_input),
        ("Sappiness", sappiness_input),
        ("Depression", depression_input),
        ("Rebellion", rebellion_input)
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

import csv
import random

def main():
    print("starting picker")
    with open('LOONA RAFFLE TRIVIA (Responses) - Form Responses 1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        total_entries = []

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            
            entrant = row["What is your name/tag (we will call this if you win the raffle so choose carefully!)"]
            score_str = row["Score"]
            score_num = int(score_str[0])
            for i in score_num:
                total_entries.append(entrant)
                i += 1

            line_count += 1

            if line_count % 10 == 0:
                print(line_count + " entrants processed. " + total_entries.count() + " entries total.")

    winners = input("Enter num of winners desired: ")
    for i in winners:
        r1 = random.randint(0, total_entries.count())
        print("winner " + i + ": " + total_entries[r1])

main()
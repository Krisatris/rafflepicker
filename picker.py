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
            for i in range(score_num):
                total_entries.append(entrant)
                i += 1

            line_count += 1

            if line_count % 10 == 0:
                print(str(line_count) + " entrants processed. " + str(len(total_entries)) + " entries total.")
    
    print("all winners processed. there are " + str(len(total_entries)) + " total entries")

    winners = input("\nEnter num of winners desired: ")

    while winners:
        winners = int(winners)
        for i in range(winners):
            print("\nthere are currently " + str(len(total_entries)) + " total entries")
            r1 = random.randint(0, len(total_entries))
            print("winner " + str(i) + ": " + total_entries[r1])
            claim = input("was the prize claimed? (y/n): ")
            if claim == 'y':
                temp_total_entries = [j for j in total_entries if j != total_entries[r1]]
                total_entries = temp_total_entries
        winners = input("Enter another number if you need more winners: ")

main()
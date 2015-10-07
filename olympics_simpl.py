"""
    Author: Ari Sanders
    Assignment: Determine information based on text file
    Date: 9/20/14
"""

def countMedalsYear(year):
    """
        Counts how many medals were won in any given year
        year = Which year to count for
    """
    year = str(year)
    olympics = open("athletes.txt", encoding="utf-8")
    medals = 0
    for line in olympics:
        if olympics.readline().strip() == year and olympics.readline().strip() == "1":
            medals += 1
    print(medals)

def countMedalsAthlete(last, first):
    """
        Counts how many of each type of medal was won
            by a given athlete over all olympics
        last = Athlete's last name
        first = Athlete's first name
    """
    olympics = open("athletes.txt", encoding="utf-8")
    gold = 0
    silver = 0
    bronze = 0
    for line in olympics:
        if olympics.readline().strip() == last.upper():
            if olympics.readline().strip() == first.upper():
                olympics.readline()
                m = olympics.readline().strip()
                if m == "1":
                    gold += 1
                elif m == "2":
                    silver += 1
                else:
                    bronze += 1
    print(first + " " + last + " won " + str(gold) + " gold, " + str(silver)
          + " silver, " + " and " + str(bronze) + " bronze medals.")

def main():
    """
        Asks users for input, then runs it through the previous functions
    """
    countMedalsYear(input("Which year should I count the medals for?: "))
    print("Which athlete should I count the medals for?")
    countMedalsAthlete(input("Last name: "), input("First name: "))
    input("Hit enter to exit.")

main()

movies = [
    {
    "movie" : "SARKAR",
    "rating" : "U",
    "tickets" : 10
    },
    {
    "movie" : "IAMK",
    "rating": "A",
    "tickets": 2
    }
]

def bookTickets(ticketCount,movieName,x):
    # print("Caleld",ticketCount)
    if ticketCount <= movies[x]['tickets']:
        movies[x]["tickets"] = movies[x]['tickets'] - ticketCount
        print("Tickets Booked")
    else:
        print("Tickets Unavailable")

while True:
    movieName = input("Which movie you wanna watch: ")

    x = 0
    while x < len(movies):
        if movies[x]['movie'] == movieName and movies[x]['rating'] == 'U':
                tickets = int(input("{} available. How many tickets do you want?".format(movies[x]['tickets'])))
                bookTickets(tickets,movieName,x)
                break
        elif movies[x]["movie"] == movieName and movies[x]['rating'] == "A":
            age = int(input("Whats is your age?: "))
            if(age >= 18):
                tickets = int(input("{} available. How many tickets do you want?".format(movies[x]['tickets'])))
                bookTickets(tickets,movieName,x)
                break
            else:
                print("You are not old enough to watch that movie")
                break
        elif x == len(movieName) - 1:
            print("We are not screening that movie")
        else:
            x = x + 1

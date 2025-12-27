       # Q1. Salman Khan’s Movie Ratings 
        # Salman Khan released 5 movies in the last 5 years. Their IMDb ratings are stored in a list: 
         # ratings = [7.1, 5.6, 6.8, 4.2, 8.3] 
         # Task: 
         # 1• Use a loop + if-else to print whether each movie was a Hit (rating ≥ 7) or Flop (rating < 7). 
        # 2• At the end, print the total number of Hits and Flops.

# movieNum = 1
# hit = 0
# flop = 0
# ratings = [7.1, 5.6, 6.8, 4.2, 8.3] 
# for i in ratings:
#     if i>7 or i>=7:
#         print(f"Movie {movieNum} : Hit")
#         hit += 1
#     else:
#         print(f"Movie {movieNum} : Flop") 
#         flop +=1 
#     movieNum += 1     
# print("Total Number of Hit moives :",hit) 
# print("Total Number of Hit moives :",flop)    



           
                # Q2. Karan Johar’s Guest List (Drama at the Party) 
                #   Karan Johar is hosting a party. The guest list is: 
                #  guests = ["Shah Rukh Khan", "Salman Khan", "Katrina Kaif", "Ranbir Kapoor", "Deepika Padukone"] 
                #  Task: 
                #  • Use a for loop to check each guest: 
                #  o If the name contains "Khan", print "VIP Guest: <name>". 
                #  o Otherwise, print "Regular Guest: <name>".

# guests = ["Shah Rukh Khan", "Salman Khan", "Katrina Kaif", "Ranbir Kapoor", "Deepika Padukone"]

# for guest in guests:
#     if "Khan" in guest:
#         print(f"VIP Guest : {guest}")
#     else:
#         print(f"Regular Guest : {guest}")
       


                #   Q3. Bollywood Box Office Collection 
                #      Suppose the collections (in crores) of Akshay Kumar’s last 6 movies are: 
                #     collections = [120, 45, 200, 95, 15, 180] 
                #     Task: 
                #    • Use a loop to count how many movies were: 
                #    o Superhit (≥100 crores) 
                #    o Average (50–99 crores) 
                #    o Flop (<50 crores) 
                #    • Print the final report.

# collections = [120, 45, 200, 95, 15, 180]
# superhit = 0
# average = 0
# flop = 0
# for amount in collections:
#     if amount >= 100:
#         superhit += 1
#     elif 50 <= amount < 100:
#         average += 1
#     else:
#         flop += 1

# print("Box Office Report:")
# print(f"Superhit Movies: {superhit}")
# print(f"Average Movies: {average}")
# print(f"Flop Movies: {flop}")



                     
                        #    Q4. Bigg Boss Elimination 
                        #      In Bigg Boss, contestants get votes. The votes list is:
                        #     votes = [250, 400, 150, 600, 320]   # each number = votes for contestant 
                        #     names = ["Arjun", "Rashmi", "Karan", "Divya", "Aly"] 
                        #     Task: 
                        #    • Use a loop to find the contestant with minimum votes (eliminated). 
                        #    • Print "Eliminated: <name>". 
                        #    • Also print "Winner till now: <name>" (the one with maximum votes). 

# votes = [250, 400, 150, 600, 320]
# names = ["Arjun", "Rashmi", "Karan", "Divya", "Aly"]
# min_votes = votes[0]
# max_votes = votes[0]
# min_index = 0
# max_index = 0
# for i in range(1, len(votes)):
#     if votes[i] < min_votes:
#         min_votes = votes[i]
#         min_index = i
#     if votes[i] > max_votes:
#         max_votes = votes[i]
#         max_index = i
# print(f"Eliminated: {names[min_index]}")
# print(f"Winner till now: {names[max_index]}")





                    #    Q5. Bollywood Song Playlist 
                    #     A playlist has songs: 
                    #     songs = ["Kesariya", "Tum Hi Ho", "Chaiyya Chaiyya", "Kabira", "Ghungroo"]
                    #     Task: 
                    #    • Ask the user to enter a song name. 
                    #    • Use a loop + condition to check if the song exists in the playlist. 
                    #    o If yes → print "Playing <song>". 
                    #    o If no → print "Song not found in playlist".

# songs = ["Kesariya", "Tum Hi Ho", "Chaiyya Chaiyya", "Kabira", "Ghungroo"]
# user_song = input("Enter a song name: ")
# found = False
# for song in songs:
#     if song == user_song: 
#         print(f"Playing :{song}")
#         found = True
#         break  
# if not found:
#     print("Song not found in playlist")




                    #  Q6. Multiplex Ticket Booking Drama 
                    #   A multiplex is screening 3 movies: 
                    #  movies = ["Pathaan", "RRR", "3 Idiots"] 
                    #  seats = [120, 80, 150]   # available seats for each movie 
                    #  Task: 
                    #  • Ask user to enter which movie they want to watch. 
                    #  • If movie exists → ask how many seats they want. 
                    #  • If enough seats available → confirm booking and reduce seats in list. 
                    #  • Else → print "Housefull! Seats not available.".

# movies = ["Pathaan", "RRR", "3 Idiots"]
# seats = [120, 80, 150]
# movie_name = input("Enter the movie you want to watch: ")
# if movie_name in movies:
#     index = movies.index(movie_name)
#     available_seats = seats[index]
#     requested_seats = int(input(f"How many seats do you want for {movie_name}? ")) 
#     if requested_seats <= available_seats:
#         seats[index] -= requested_seats  # reduce seats
#         print(f"Booking confirmed for {requested_seats} seats for '{movie_name}'.")
#     else:
#         print("Housefull! Seats not available.")
# else:
#     print("Movie not found.")




  
                        #        Q7. Bollywood Family Feud (Kapoor Clan) 
                        #           The Kapoor family has ages stored: 
                        #           kapoors = [65, 60, 35, 30, 25, 20]   
                        #           Task: 
                        #          • Write a program using loop + if-else: 
                        #          o Count how many are Seniors (age ≥ 60)
                        #          o Count how many are Adults (18–59) 
                        #          o Count how many are Kids (<18) 
                        #          • Print family age report.

# kapoors = [65, 60, 35, 30, 25, 20]
# seniors = 0
# adults = 0
# kids = 0
# for age in kapoors:
#     if age >= 60:
#         seniors += 1
#     elif 18 <= age <= 59:
#         adults += 1
#     else:
#         kids += 1
# print("Kapoor Family Age Report:")
# print(f"Seniors (60 and above): {seniors}")
# print(f"Adults (18 to 59): {adults}")
# print(f"Kids (below 18): {kids}")



                    
                        #       Q8. Award Night – Best Actor Voting 
                        #        Actors and votes received: 
                        #        actors = ["Ranbir", "Ranveer", "Varun", "Ayushmann", "Rajkummar"] 
                        #        votes = [350, 420, 120, 400, 390] 
                        #          Task: 
                        #        • Find the actor with highest votes (Winner). 
                        #        • Find the actor with second highest votes (Runner-up). 
                        #        • Print both names with votes. 
                        #         (Hint: use loops instead of direct max() for practice.)

# actors = ["Ranbir", "Ranveer", "Varun", "Ayushmann", "Rajkummar"]
# votes = [350, 420, 120, 400, 390]
# sorted_votes = sorted(votes, reverse=True) 
# winner_vote = sorted_votes[0]
# winner_actor = actors[votes.index(winner_vote)]

# runnerup_vote = sorted_votes[1]
# runnerup_actor = actors[votes.index(runnerup_vote)]
# print(f"Largest votes: {runnerup_vote} by {winner_actor}")
# print(f"Second largest votes: {runnerup_vote} by {runnerup_actor}")


# actors = ["Ranbir", "Ranveer", "Varun", "Ayushmann", "Rajkummar"]
# votes = [350, 420, 120, 400, 390]
# max_vote = -1
# second_max_vote = -1
# max_actor = ""
# second_max_actor = ""
# for i in range(len(votes)):
#     if votes[i] > max_vote:
#         second_max_vote = max_vote
#         second_max_actor = max_actor

#         max_vote = votes[i]
#         max_actor = actors[i]

#     elif votes[i] > second_max_vote:
#         second_max_vote = votes[i]
#         second_max_actor = actors[i]

# print(f"Largest votes: {max_vote} by {max_actor}")
# print(f"Second largest votes: {second_max_vote} by {second_max_actor}")




                        #    Q9. Koffee with Karan – Rapid Fire Round 
                        #      Guests answered with these scores: 
                        #     scores = [10, 15, 8, 20, 18]   
                        #     guests = ["Alia", "Kareena", "Priyanka", "Deepika", "Katrina"] 
                        #      Task: 
                        #    • Total Rapid Fire prize = 50,000 INR. 
                        #    • Winner (highest score) gets 60% of prize. 
                        #    • Runner-up (second highest) gets 30%. 
                        #    • Rest share remaining 10% equally. 
                        #    • Print each guest with amount won.

# scores = [10, 15, 8, 20, 18]
# guests = ["Alia", "Kareena", "Priyanka", "Deepika", "Katrina"]
# total_prize = 50000
# max_score = max(scores)
# scores_copy = scores.copy()
# scores_copy.remove(max_score)
# second_max_score = max(scores_copy)
# for i in range(len(guests)):
#     if scores[i] == max_score:
#         amount = 0.60 * total_prize
#     elif scores[i] == second_max_score:
#         amount = 0.30 * total_prize
#     else:
#         amount = (0.10 * total_prize) / (len(guests) - 2)
#     print(f"{guests[i]} wins {amount:.2f} INR")






                        #    Q10. Bollywood Music Launch – Streaming Analysis 
                        #     A new album has streaming counts (in millions): 
                        #     songs = ["Kesariya", "Apna Bana Le", "Natu Natu", "Tere Vaaste", "Pasoori"] 
                        #     streams = [95, 120, 300, 80, 150] 
                        #     Task: 
                        #     • Use loop + conditions to categorize:
                        #     o Superhit (≥200M) 
                        #     o Hit (100M–199M) 
                        #     o Average (<100M) 
                        #     • Store songs in separate lists for each category. 
                        #     • Print all three category lists.

# songs = ["Kesariya", "Apna Bana Le", "Natu Natu", "Tere Vaaste", "Pasoori"]
# streams = [95, 120, 300, 80, 150]

# superhit = []
# hit = []
# average = []

# for i in range(len(songs)):
#     if streams[i] >= 200:
#         superhit.append(songs[i])
#     elif 100 <= streams[i] <= 199:
#         hit.append(songs[i])
#     else:
#         average.append(songs[i])

# print("Superhit songs:", superhit)
# print("Hit songs:", hit)
# print("Average songs:", average)



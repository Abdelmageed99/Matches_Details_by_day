from bs4 import BeautifulSoup
import requests
import pandas as pd 
import csv


# first step
date = input("enter a Date in the following format MM-DD-YYYY:")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#")
# print(page)


def matchesInfo(page) :

      src = page.content
      # print(src)       


      soup = BeautifulSoup(src, 'lxml')
      # print(soup)

      matches_details = []


      championships = soup.find_all("div",{'class' : 'matchCard'})
      # print(championship)
      # print(len(championships))
      
      for champ in range(len(championships)):

        championship_title = championships[champ].contents[1].find("h2").text.strip()
      #   print(championship_title)
        all_matches = championships[champ].contents[3].find_all("div", {"class" : "item"})
      #   print(all_matches)
        num_of_matches = len(all_matches)
        # print(num_of_matches)

        for i in range(num_of_matches) :
              
              # get teams's Names
              teamA = all_matches[i].find("div" , {"class" : "teamA"}).find("p").text.strip()
              # print(teamA)
              teamB = all_matches[i].find("div" , {"class" : "teamB"}).find("p").text.strip()
              # print(teamB)

              # get result
              match_result = all_matches[i].find("div" , {"class" : "MResult"}).find_all("span", {"class" : "score"})
              # print(match_rCesult)
              score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            #   print(score)


              # # get match time
              match_time = all_matches[i].find("div" , {"class" : "MResult"}).find("span", {"class" : "time"}).text.strip()
              # print(match_time)


              # # add match info to match_details

              matches_details.append({"نوع البطوله" : championship_title, "الفريق الأول" : teamA, 
                                     "الفريق الثانى" : teamB, "النتيجه" : score, "ميعاد المباراة" : match_time})
              
      #print(matches_details)
      Matches = pd.DataFrame.from_dict(matches_details)
      # print(Matches.head())
      # Matches.to_csv("Matches.csv", index = False)
      Matches.to_excel(f"YallaKora{date}.xlsx", index = False)



matchesInfo(page)     


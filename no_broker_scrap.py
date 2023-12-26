import json
import requests
import pandas as pd


api_url = "https://www.nobroker.in/api/v1/multi/property/sale/filter"

query = {
    "pageNo": 0,
    "searchParam": "W3sibGF0IjoxOC42Mzg2NTE3LCJsb24iOjczLjc5NTE1NzMsInBsYWNlSWQiOiJDaElKb2RIRFU2VzV3anNSaUpIZ01YYVVucHMiLCJwbGFjZU5hbWUiOiJDaGluY2h3YWQifSx7ImxhdCI6MTguNjUwNDgzOSwibG9uIjo3My43Nzg1Nzg2LCJwbGFjZUlkIjoiQ2hJSnktaFVLY0M1d2pzUjhpYlY0WTF3WFZJIiwicGxhY2VOYW1lIjoiQWt1cmRpIn0seyJsYXQiOjE4LjY0OTE3MzUsImxvbiI6NzMuNzcwNjUzMiwicGxhY2VJZCI6IkNoSUp1X255Yk9lNXdqc1J5TWE4SWRHbXdsRSIsInBsYWNlTmFtZSI6Ik5pZ2RpIn1d&",
    "radius": "2.0",
    "city": ["pune", "pune"],
    "locality": ("Chinchwad","Akurdi","Nigdi")
}

# https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC42Mzg2NTE3LCJsb24iOjczLjc5NTE1NzMsInBsYWNlSWQiOiJDaElKb2RIRFU2VzV3anNSaUpIZ01YYVVucHMiLCJwbGFjZU5hbWUiOiJDaGluY2h3YWQifSx7ImxhdCI6MTguNjUwNDgzOSwibG9uIjo3My43Nzg1Nzg2LCJwbGFjZUlkIjoiQ2hJSnktaFVLY0M1d2pzUjhpYlY0WTF3WFZJIiwicGxhY2VOYW1lIjoiQWt1cmRpIn0seyJsYXQiOjE4LjY0OTE3MzUsImxvbiI6NzMuNzcwNjUzMiwicGxhY2VJZCI6IkNoSUp1X255Yk9lNXdqc1J5TWE4SWRHbXdsRSIsInBsYWNlTmFtZSI6Ik5pZ2RpIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Chinchwad,Akurdi,Nigdi


all_data, page = [], 0
while True:
    print("Getting page. {}".format(page))
    query["pageNo"] = page
    data = requests.get(api_url, params=query).json()
    # print(data)
    # save json data in json file 
    

    if not data["data"]:
        break

    # uncomment this to print all data:
    print(json.dumps(data, indent=4))
    # save_file = open("savedata.json", "w")  
    # json.dumps(data, indent = 6)  
    # save_file.close()
    

    for p in data["data"]:
        all_data.append(
            {
                "house_title": p["propertyTitle"],
                "location": p["locality"],
                "emi": p["defaultEmi"],
                "price": p["price"],
                "bathroom": p["bathroom"],
                "parking": p["parking"],
                "localityTruncated": p["localityTruncated"],
                "propertyType": p["propertyType"],
                "state": p["state"],
                "typeDesc": p["typeDesc"],
                "propertySize":p["propertySize"],
            }
        )

    page += 1

df = pd.DataFrame(all_data)
print(df)
df.to_csv("data.csv", index=False)
import requests

class IRCTC:
    def __init__(self):
        user_input = input("""How Would you like to proceed?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule""")

        if user_input == "1":
            print("Live Train Status :")
        elif user_input == "2":
            print("PNR")
        else:
            self.train_schedule()
    
    def train_schedule(self):
        train_no = input('Enter the Train No :')
        self.fetch_data(train_no)
    
    def fetch_data(self,train_no):
        # url = "https://irctc1.p.rapidapi.com/api/v1/getTrainSchedule"
        data = requests.get("https://indianrailapi.com.api/v2/TrainSchedule/apikey/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}".format(train_no))
        data = data.json()
        print(data['Route'])
        for i in data['Route']:
            print(i['StationName'],"|",i['ArrivalTime'],"|",i['DepartureTime'],"|",i['Distance'])

obj = IRCTC()
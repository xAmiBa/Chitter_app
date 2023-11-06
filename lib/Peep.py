from datetime import datetime

class Peep:
    def __init__(self, id, content, user_id, likes=0, date_time=None):
        if date_time == None:
            current_date_time = datetime.now()
            self.date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date_time = date_time

        self.id = id
        self.content = content
        self.user_id = user_id
        self.likes = likes

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
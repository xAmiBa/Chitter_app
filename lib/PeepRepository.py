# 
from lib.Peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_date_time(peep):
            return peep.date_time

    def all(self, get_date_time=get_date_time):
        rows = self._connection.execute("SELECT * FROM peeps;")
        peeps = [Peep(row['id'], row['content'], row['user_id'], row['date_time']) for row in rows]

        sorted_peeps = sorted(peeps, key=get_date_time, reverse=True)
        return sorted_peeps

    def add(self, peep_object):
        self._connection.execute("INSERT INTO peeps (content, user_id, date_time) VALUES (%s, %s, %s);",
                                 [peep_object.content, peep_object.user_id, peep_object.date_time])

    def search_for_mention(self, username):
        peeps = self.all()
        username = "@" + username
        mentions = [peep for peep in peeps if username in peep.content]
        return mentions
    
    def get_author(peep):
         pass
                  
             
        
    

# 
from lib.Peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM peeps;")
        peeps = [Peep(row['id'], row['content'], row['user_id'], row['date_time']) for row in rows]
        return peeps

    def add(self, peep_object):
        self._connection.execute("INSERT INTO peeps (content, user_id, date_time) VALUES (%s, %s, %s);",
                                 [peep_object.content, peep_object.user_id, peep_object.date_time])


    #     pass
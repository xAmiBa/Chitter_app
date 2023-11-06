# 
from lib.Peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_date_time(peep):
            return peep.date_time

    def all(self, get_date_time=get_date_time):
        rows = self._connection.execute("SELECT * FROM peeps;")
        peeps = [Peep(row['id'], row['content'], row['user_id'], row['likes'], row['date_time']) for row in rows]

        sorted_peeps = sorted(peeps, key=get_date_time, reverse=True)
        return sorted_peeps

    def add(self, peep_object):
        self._connection.execute("INSERT INTO peeps (content, user_id, likes, date_time) VALUES (%s, %s, %s, %s);",
                                 [peep_object.content, peep_object.user_id, peep_object.likes, peep_object.date_time])

    def search_for_mention(self, username):
        peeps = self.all()
        username = "@" + username
        mentions = [peep for peep in peeps if username in peep.content]
        return mentions
    
    def get_author(peep):
         pass

    # when post id specified, one like is added
    def add_like(self, post_id):
        try:
            rows = self._connection.execute("SELECT likes FROM peeps WHERE id=%s", [post_id])
            count = rows[0]['likes']
            count = count + 1
            self._connection.execute("UPDATE peeps SET likes=%s WHERE id=%s", [count, post_id])
        # if post doesn't exists nothing happens
        except:
            pass
    
    # when post id specified, one like is removed
    def remove_like(self, post_id):
        try:
            rows = self._connection.execute("SELECT likes FROM peeps WHERE id=%s", [post_id])
            count = rows[0]['likes']
            count = count - 1
            self._connection.execute("UPDATE peeps SET likes=%s WHERE id=%s", [count, post_id])
        except:
            pass

    # when post id is specified returns number of likes
    def count_likes(self, post_id):
        try:
            rows = self._connection.execute("SELECT likes FROM peeps WHERE id=%s", [post_id])
            count = rows[0]['likes']
            return count
        except:
            pass

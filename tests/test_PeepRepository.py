from lib.Peep import Peep
from lib.PeepRepository import PeepRepository

def test_all_peeps_show(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    
    assert repository.all() == [
        Peep(1, 'I learned SQL today, it was fun!', 1,'2022-10-10 12:24:55'),
        Peep(2, 'What a day, 5k run done!', 2, '2022-10-17 12:24:55'),
        Peep(3, 'Boris Johnson is crazy...', 3, '2022-10-11 18:24:55'),
        Peep(4, 'Anyone knows good restaurants in Central London?', 1, '2022-10-14 16:24:55'),
        Peep(5, '#partytime Happy bDay to me!', 2, '2022-10-12 13:24:55')]
    
def test_add_new_peep(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    repository.add(Peep(None, "Test peep content", 1, "2012-10-10 12:24:55"))
    
    assert repository.all() == [
        Peep(1, 'I learned SQL today, it was fun!', 1,'2022-10-10 12:24:55'),
        Peep(2, 'What a day, 5k run done!', 2, '2022-10-17 12:24:55'),
        Peep(3, 'Boris Johnson is crazy...', 3, '2022-10-11 18:24:55'),
        Peep(4, 'Anyone knows good restaurants in Central London?', 1, '2022-10-14 16:24:55'),
        Peep(5, '#partytime Happy bDay to me!', 2, '2022-10-12 13:24:55'),
        Peep(6, "Test peep content", 1, "2012-10-10 12:24:55")]
    
        
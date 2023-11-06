from lib.Peep import Peep
from lib.PeepRepository import PeepRepository

def test_all_peeps_show(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    
    assert repository.all() == [
        Peep(2, 'What a day, 5k run done! @xAmiBa', 2, 20,'2022-10-17 12:24:55'),
        Peep(4, 'Anyone knows good restaurants in Central London?', 1, 40, '2022-10-14 16:24:55'),
        Peep(5, '#partytime Happy bDay to me!', 2, 50, '2022-10-12 13:24:55'),
        Peep(3, 'Boris Johnson is crazy...', 3, 30, '2022-10-11 18:24:55'),
        Peep(1, 'I learned SQL today, it was fun!', 1, 10, '2022-10-10 12:24:55')]
    
def test_add_new_peep(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    repository.add(Peep(None, "Test peep content", 1, 0, "2012-10-10 12:24:55"))
    
    assert repository.all() == [
        Peep(2, 'What a day, 5k run done! @xAmiBa', 2, 20,'2022-10-17 12:24:55'),
        Peep(4, 'Anyone knows good restaurants in Central London?', 1, 40, '2022-10-14 16:24:55'),
        Peep(5, '#partytime Happy bDay to me!', 2, 50, '2022-10-12 13:24:55'),
        Peep(3, 'Boris Johnson is crazy...', 3, 30, '2022-10-11 18:24:55'),
        Peep(1, 'I learned SQL today, it was fun!', 1, 10, '2022-10-10 12:24:55'),
        Peep(6, "Test peep content", 1, 0, "2012-10-10 12:24:55")]
    
def test_if_mentioned(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    assert repository.search_for_mention("xAmiBa") == [Peep(2, 'What a day, 5k run done! @xAmiBa', 2, 20, '2022-10-17 12:24:55')]

def test_if_like_added(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    repository.add_like(1)
    assert repository.count_likes(1) == 11

def test_if_like_removed(db_connection):
    db_connection.seed('seeds/chitter.sql')
    repository = PeepRepository(db_connection)
    repository.remove_like(2)
    assert repository.count_likes(2) == 19

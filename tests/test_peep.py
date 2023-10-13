from lib.Peep import Peep

def test_peep_created():
    peep = Peep(None, "Test peep content", 1, "2012-10-10 12:24:55")
    assert peep.id == None
    assert peep.content == "Test peep content"
    assert peep.date_time == "2012-10-10 12:24:55"
    assert peep.user_id == 1

def test_peep_equal():
    peep1 = Peep(None, "Test peep content", 1, "2012-10-10 12:24:55")
    peep2 = Peep(None, "Test peep content", 1, "2012-10-10 12:24:55")
    assert peep1 == peep2


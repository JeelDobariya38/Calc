from Calc.calc import calc_execute

def test_calc_whitespace_comptablity():
    assert calc_execute("") == ""
    assert calc_execute("   ") == ""
    assert calc_execute("\t") == ""
    assert calc_execute("\n") == ""
    assert calc_execute("\n \t \n     \t") == ""

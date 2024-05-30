from calc import calc_execute


def test_addition_of_numbers():
  res1 = calc_execute("1 + 1")
  res2 = calc_execute("1 + -4 + 6")
  res3 = calc_execute("6 + 7 + 8")
  res4 = calc_execute("8.5 + 5.4  + 3")
  res5 = calc_execute("-8.5 + 7")

  assert res1 == 2.0
  assert res2 == 3.0
  assert res3 == 21.0
  assert res4 == 16.9
  assert res5 == -1.5


def test_subtraction_of_numbers():
  res1 = calc_execute("1 - 1")
  res2 = calc_execute("1 - 4 - 6")
  res3 = calc_execute("16 - 7 - -8")
  res4 = calc_execute("8.5 - 5.4  - 3")

  assert res1 == 0.0
  assert res2 == -9.0
  assert res3 == 17.0
  assert round(res4) == 0

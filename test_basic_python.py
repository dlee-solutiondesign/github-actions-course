def inc(x):
  return x+1

def test_answer():
  assert inc(3) == 4

res = inc(2)

print("The increment of 2 is {}".format(res))

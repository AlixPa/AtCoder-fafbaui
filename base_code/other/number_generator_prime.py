MAX_NUMBER = 10
PRIME_LIST = [2, 3, 5, 7] #continue to last prime of MAX_NUMBER
NUMBER_LIST = [1]

class generateAllNumbersFromPrime:
  def __init__(self, mult_cur, index_cur):
    self.mult_cur = mult_cur
    self.index_cur = index_cur

  def next_step(self):
    global MAX_NUMBER
    global PRIME_LIST
    global NUMBER_LIST

    NUMBER_LIST.append(self.mult_cur)

    for i in range(self.index_cur, len(PRIME_LIST)):
      mult_tmp = self.mult_cur * PRIME_LIST[i]
      if mult_tmp > MAX_NUMBER:
        return
      new_generateAll = generateAllNumbersFromPrime(mult_tmp, i)
      new_generateAll.next_step()

for i in range(len(PRIME_LIST)):
  new_generate = generateAllNumbersFromPrime(PRIME_LIST[i], i)
  new_generate.next_step()

NUMBER_LIST.sort()
print(NUMBER_LIST)
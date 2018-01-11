def myavg():
   total = 0.0
   count = 0
   average = 100
   while True:
      term = yield average
      total += term
      count += 1
      average = total/count


cavg = myavg()
print next(cavg)
print cavg.send(10)
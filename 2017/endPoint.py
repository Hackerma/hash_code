def getKey(item):
  return item[1]

class endPoint:
  def __init__(self, lat1):
    self.lat1 = lat1
    self.list = []

  def addCacheLat(self, lat, cache):
     self.list.append((cache,lat))

  def savingLat(self):
    Length = len(self.list)
    savings = [0] * Length
    for i in range(Length):
      latSaved = self.lat1 - self.list[i][1]
      savings[i] = (self.list[i][0], latSaved)

    sorted(savings, key = getKey)
    return savings

  def disp(List):
    for i in range(len(List)):
      print(List[i][1])


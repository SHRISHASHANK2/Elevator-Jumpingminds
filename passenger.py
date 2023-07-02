class Passenger:
    def __init__(self, arrTime, depTime=None, getOnTime=None, y1=None, y2=None, _id=None, choiceElv=None):
        self.arrTime = arrTime
        self.depTime = depTime
        self.getOnTime = getOnTime
        self.y1 = y1
        self.y2 = y2
        self._id = _id
        self.choiceElv = choiceElv
        
    def __repr__(self):
        return '"psg #{}"'.format(self._id)

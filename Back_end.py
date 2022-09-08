class Round:
    def __init__(self, r):
        self.round = r
        self.bonus = 20

        for i in range(0, r if r < 20 else 20):
            self.bonus += 20
        if r > 20:
            for i in range(20, r if r < 50 else 50):
                self.bonus += 40
        if r > 50:
            for i in range(50, r):
                self.bonus += 90

    def roundup(self):
        self.round += 1
        self.bonus += 20 if self.round < 21 else 40 if self.round < 51 else 90

    def __eq__(self, other):
        return self.round == other.r


class Game:
    def __init__(self, firstr: Round, finalr: Round):
        self.firstR = firstr
        self.finalR = finalr
        self.currentRound = firstr
        self.xpForGame = 0
        self.gotXP = 0
        for i in range(self.firstR.round, self.finalR.round + 1):
            self.xpForGame += firstr.bonus
            firstr.roundup()

    def roundup(self):
        self.gotXP += self.currentRound.bonus
        self.currentRound.roundup()

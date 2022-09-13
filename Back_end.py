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
        return self.round == other.round

    def __gt__(self, other):
        return self.round > other.round


class Game:
    def __init__(self, firstr: Round, finalr: Round, difb: float = 1):
        self.firstR = Round(firstr.round)
        self.finalR = Round(finalr.round)
        self.currentRound = Round(firstr.round)
        self.mapDifBonus = difb
        self.xpForGame = 0
        self.gotXP = 0
        for i in range(self.firstR.round, self.finalR.round + 1):
            self.xpForGame += int(firstr.bonus * difb)
            firstr.roundup()

    def roundup(self):
        self.gotXP += int(self.currentRound.bonus * self.mapDifBonus * (0.1 if self.currentRound > self.finalR else 1))
        self.currentRound.roundup()

    def xptoandfromround(self, firstr: int, finalr: int):
        temp = Game(self.firstR, self.finalR, self.mapDifBonus)

        if temp.currentRound.round == firstr:
            nothing = 0
            """print("obj firstr = firstr par")"""
        elif temp.currentRound.round > firstr:
            assert "first round must be more"
            """print("first round must be more")"""
        else:
            while temp.currentRound.round < firstr:
                temp.roundup()
                """print("round upped\n" + "current round: " + str(temp.currentRound.round) + "\nfirst round: " + str(firstr) + "\n\n")"""

        temp.gotXP = 0

        for i in range(firstr, finalr + 1):
            temp.roundup()
            """
            print("round upped\n" + "current round: " + str(temp.currentRound.round) + "\nfirst round: " + str(finalr) + "\n")
            print("xp bonus: " + str(temp.currentRound.bonus) + "\ngotXP: " + str(temp.gotXP) + "\n\n")"""
        return temp.gotXP

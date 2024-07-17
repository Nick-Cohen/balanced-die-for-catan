import random

class Balanced_die:
    def __init__(self):
        self.prolls_expected = {
            2:1/36,
            3:2/36,
            4:3/36,
            5:4/36,
            6:5/36,
            7:6/36,
            8:5/36,
            9:4/36,
            10:3/36,
            11:2/36,
            12:1/36,
        }
        self.prolls = {
            2:1/36,
            3:2/36,
            4:3/36,
            5:4/36,
            6:5/36,
            7:6/36,
            8:5/36,
            9:4/36,
            10:3/36,
            11:2/36,
            12:1/36,
        }
        self.roll_counts = {k:6*self.prolls[k] for k in list(self.prolls.keys())}
        self.num_rolls = sum([self.roll_counts[k] for k in list(self.roll_counts.keys())])
        
    def roll(self):
        r = random.random()
        s = 0
        roll = 2
        while s < r:
            s += self.prolls[roll]
            roll += 1
        roll -= 1
        self.adjust_prolls(roll)
        return roll
    
    def adjust_prolls(self, roll):
        self.num_rolls += 1
        self.roll_counts[roll] += 1
        nums = [i for i in range(2,13)]
        unnorm_prolls = {n: self.prolls_expected[n]**2/self.roll_counts[n] for n in nums}
        Z = sum([unnorm_prolls[n] for n in nums])
        for n in nums:
            self.prolls[n] = unnorm_prolls[n]/Z
    
    def test_rolls(self, nsamples=100000):
        rolls = {i:0 for i in range(2,13)}
        for i in range(nsamples):
            r = self.roll()
            try:
                rolls[r] += 1
            except:
                print('r is ', r)
        for k in list(rolls.keys()):
            print(k, ": ", rolls[k]/nsamples)

def wait_for_enter():
    input("Press Enter to roll the die...")

if __name__ == "__main__":
    bd = Balanced_die()
    while True:
        wait_for_enter()
        print(bd.roll())

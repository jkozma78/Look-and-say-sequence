class LookAndSaySequence:
    def __init__(self, input, seq):
        self.input = input
        self.count = 0
        self.conway = ""
        self.currentnumber = input[0]
        self.seq = seq
        self.sequence()

    def __str__(self):
        return self.input

    def __len__(self):
        return len(self.input)

    def sequence(self):
        print(self.input)

        for n in range(1, self.seq):
            for i in range(len(self.input)):
                if self.input[i] == self.currentnumber:
                    self.count += 1
                else:
                    self.conway = self.conway + str(self.count) + self.currentnumber
                    self.currentnumber = self.input[i]
                    self.count = 1
                if i == len(self.input) - 1:
                    self.conway = self.conway + str(self.count) + self.currentnumber

            print(self.conway)
            self.input = self.conway
            self.count = 0
            self.conway = ""
            self.currentnumber = self.input[0]

        return input

class LookAndSaySequence:
    """This class is calculating Look-and-say sequence. The first argument is the first number of sequence.
    This method can return the elements(th) of the second argument or its' length."""

    def __init__(self, start_number, elements):
        """Init the arguments"""
        self.start_number = str(start_number)  # the first number of sequence
        self.number_count = 0  # counting the number
        self.conway = ""  # created conway number
        self.current_number = self.start_number[0]  # the actual number to count
        self.elements = elements  # elements(th) number of sequence
        self.calculation()  # call the function, what is able to calculate the elements(th) number of conway sequence

    def __str__(self):
        return self.start_number

    def __len__(self):
        return len(self.start_number)

    def calculation(self):
        """Calculate the conway sequence"""
        for n in range(1, self.elements):
            # calculate the self.elements(th) number
            for i in range(len(self.start_number)):
                if self.start_number[i] == self.current_number:
                    self.number_count += 1
                else:
                    self.conway = self.conway + str(self.number_count) + self.current_number
                    self.current_number = self.start_number[i]
                    self.number_count = 1
                if i == len(self.start_number) - 1:
                    self.conway = self.conway + str(self.number_count) + self.current_number
            # reset these variables
            self.start_number = self.conway
            self.number_count = 0
            self.conway = ""
            self.current_number = self.start_number[0]

        return self.start_number

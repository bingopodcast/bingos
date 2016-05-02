import random

class Stepper:
    def __init__(self, name, top, gamename=None):
        self.name = name
        self.position = 0
        self.horizontal = 0
        self.vertical = 0
        self.diagonal = 0
        self.four = 0
        self.five = 0
        self.top = top
        self.gamename = gamename
        if self.name == "odds":
            if gamename == "spot_lite":
                self.horizontal = self.get_horizontal()
                self.vertical = self.get_vertical()
                self.diagonal = self.get_diagonal()
                self.four = self.get_four()
                self.five = self.get_five()
    def step(self):
        if self.position != self.top:
            self.position += 1
            if self.name == 'odds':
                if self.gamename == "spot_lite":
                    self.horizontal = self.get_horizontal()
                    self.vertical = self.get_vertical()
                    self.diagonal = self.get_diagonal()
                    self.four = self.get_four()
                    self.five = self.get_five()
        return self.position
    def reset(self):
        self.position = 0
        return self.position
    def get_horizontal(self):
        if self.position == 1:
            return 2
        elif self.position == 2:
            return 4
        elif self.position == 3:
            return 6
        elif self.position == 4:
            return 8
        elif self.position == 5:
            return 12
        elif self.position == 6:
            return 16
        elif self.position == 7:
            return 24
        elif self.position == 8:
            return 32
        elif self.position == 9:
            return 48
        elif self.position == 10:
            return 64
    def get_vertical(self):
        if self.position == 1:
            return 4
        elif self.position == 2:
            return 6
        elif self.position == 3:
            return 8
        elif self.position == 4:
            return 12
        elif self.position == 5:
            return 16
        elif self.position == 6:
            return 24
        elif self.position == 7:
            return 32
        elif self.position == 8:
            return 48
        elif self.position == 9:
            return 64
        elif self.position == 10:
            return 96
    def get_diagonal(self):
        if self.position == 1:
            return 6
        elif self.position == 2:
            return 8
        elif self.position == 3:
            return 12
        elif self.position == 4:
            return 16
        elif self.position == 5:
            return 24
        elif self.position == 6:
            return 32
        elif self.position == 7:
            return 48
        elif self.position == 8:
            return 64
        elif self.position == 9:
            return 96
        elif self.position == 10:
            return 128
    def get_four(self):
        if self.position == 1:
            return 8
        elif self.position == 2:
            return 16
        elif self.position == 3:
            return 24
        elif self.position == 4:
            return 32
        elif self.position == 5:
            return 48
        elif self.position == 6:
            return 64
        elif self.position == 7:
            return 96
        elif self.position == 8:
            return 128
        elif self.position == 9:
            return 160
        elif self.position == 10:
            return 200
    def get_five(self):
        if self.position == 1:
            return 50
        elif self.position == 2:
            return 50
        elif self.position == 3:
            return 50
        elif self.position == 4:
            return 100
        elif self.position == 5:
            return 100
        elif self.position == 6:
            return 200
        elif self.position == 7:
            return 200
        elif self.position == 8:
            return 200
        elif self.position == 9:
            return 200
        elif self.position == 10:
            return 200

class Mixer:
    def __init__(self, name, top):
        self.name = name
        self.position = 0
        self.top = top
    def spin(self):
        if self.name != "mixer1":
            movement_amount = random.choice([1-self.top])
        else:
            movement_amount = 1
        self.position += movement_amount
        if self.position + movement_amount > self.top:
            self.position -= self.top
        return self.positon
    def connected_rivet(self):
        # Here's the sticky part - we have to identify the wire that is connected.  Looking at the schematic of the mixer,
        # it appears that there are three different wires that allow current to pass through the unit.  For Coney Island
        # these wires are 14-3, 15-3 and 18-3. Based on other early Bally mixers, it appears that there are three dead
        # (disconnected) rivets. 0 maps to a dead rivet, 1 maps to 14-3, 2 maps to 15-3 and 3 maps to 18-3. Note that I
        # can only add this to the base Mixer class on games like Coney Island that have a single mixer unit.
        if self.position % 5:
            return 0
        elif self.position % 4:
            return 1
        elif self.position % 3:
            return 2
        elif self.position % 2:
            return 3

class Search:
	def __init__(self, name, top):
            self.name = name
            self.position = 0
            self.top = top
	def spin(self):
            if self.position + 1 > self.top:
                self.position -= self.top
            else:
                self.position += 1
            return self.position
        def connected_rivet(self):
            return self.position

class Relay:
    def __init__(self, name):
        self.name = name
        self.status = False
    def engage(self, game):
        if self.name == "replay_reset":
            game.coils.registerDown.pulse()
        self.status = True
        return self.status
		#play a small buzzing noise - not huge, but enough to hear if you're listening for it.
    def disengage(self):
        self.status = False
        return self.status

class Reflex:
    def __init__(self, name, top):
        self.name = name
        self.position = 50
        self.top = top
    def increase(self):
        self.position += 2
        return self.position
    def decrease(self):
        self.position -= 1
        return self.position
    def connected_rivet(self):
        # See my mixer comments above - in this case, the mixer has four different rivets. unlike the mixer though, the
        # reflex wll connect up to all four rivets at once.  On the reflex, the last rivet onnected will actually bypass
        # the mixer, so there is no need to check the mixer depending on which rivets are returned.  The mixer will not
        # prevent the step of the EB unit if the reflex is connected on all four rivets.  If the reflex is on only three
        # rivets, the mixer is essentially bypassed, unless the mixer.connected_rivet() == 0.  The reflex can actually
        # step beyond the last rivet, which means that the machine is as tight as it can possibly be - it will be very
        # difficult to get an extra ball. The common feeds into the reflex, and it outputs on the same 14-3, 15-3 and 18-3
        # used by the mixer unit, however, there is also that bypass rivet with wire 21-3.
        if self.position > 200:
            return 0
        elif self.position <= 50:
            return 4
        elif self.position <= 100:
            return 3
        elif self.position <= 150:
            return 2
        elif self.position <= 200:
            return 1

import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        time = 0
        while self.distance > 0:
            for runner in self.runners:
                distance_run = min(self.distance, runner.speed)
                runner.distance += distance_run
                self.distance -= distance_run
                if self.distance <= 0:
                    break
            time += 1
        return max(self.runners, key=lambda x: x.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(value)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.andrey, self.nick])
        winner = tournament.start()
        self.assertEqual(winner.name, "Андрей")

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.usain, self.nick])
        winner = tournament.start()
        self.assertEqual(winner.name, "Усэйн")

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, [self.usain, self.andrey, self.nick])
        winner = tournament.start()
        self.assertEqual(winner.name, "Усэйн")




if __name__ == '__main__':
    unittest.main()

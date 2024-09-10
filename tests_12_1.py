import TestCase
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = TestCase.Runner("Home")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance,50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner2 = TestCase.Runner("Rabbit")
        for i in range(10):
            runner2.run()
        self.assertEqual(runner2.distance,100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner3 = TestCase.Runner("Orange")
        runner4 = TestCase.Runner("Apple")
        for i in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance,runner4.distance)

if __name__ == '__main__':
    unittest.main()

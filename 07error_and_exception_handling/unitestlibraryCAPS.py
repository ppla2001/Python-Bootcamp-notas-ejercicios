import unittest
import unitestlibrarycap #me conviene hacerlo desde desktop para no tener problemas insertando la carpeta antes de unites... significa q deberia mover el otro archivo tambien a desktop

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = unitestlibrarycap.cap_text
        self.assertSetEqual(result,'Python')

        def test_multiple_words(self):
            text = 'monty python'
            result = unitestlibrarycap.cap_text
            self.assertSetEqual(result,'Monty Python')

if __name__ == "__main__":
    unittest.main()
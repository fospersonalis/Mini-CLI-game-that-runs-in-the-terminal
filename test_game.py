import unittest
from unittest.mock import patch
from io import StringIO
import game

class TestGame(unittest.TestCase):

    @patch('random.randint', return_value=50)
    @patch('builtins.input', side_effect=['40', '60', '50'])
    def test_play_game_win(self, mock_input, mock_randint):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.play_game()
            output = fake_out.getvalue()
            self.assertIn("Too low!", output)
            self.assertIn("Too high!", output)
            self.assertIn("Congratulations! You guessed the number, which was 50.", output)

    @patch('random.randint', return_value=50)
    @patch('builtins.input', side_effect=['abc', '50'])
    def test_play_game_invalid_input(self, mock_input, mock_randint):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.play_game()
            output = fake_out.getvalue()
            self.assertIn("Invalid input. Please enter a whole number.", output)
            self.assertIn("Congratulations! You guessed the number, which was 50.", output)

    @patch('random.randint', return_value=50)
    @patch('builtins.input', side_effect=['0', '101', '50'])
    def test_play_game_out_of_range(self, mock_input, mock_randint):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.play_game()
            output = fake_out.getvalue()
            self.assertIn("Your guess must be between 1 and 100.", output)
            self.assertIn("Congratulations! You guessed the number, which was 50.", output)

if __name__ == '__main__':
    unittest.main()

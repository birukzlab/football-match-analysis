import unittest
from src.data_processing import preprocess_data
import pandas as pd

class TestDataProcessing(unittest.TestCase):
    
    def test_preprocess_data(self):
    
        mock_data = pd.DataFrame({
            'type': ['Pass', 'Pass', 'Shot'],
            'location': [[10, 20], [15, 25], [30, 40]],
            'player_name': ['Player 1', 'Player 2', 'Player 3']
        })
        
        # Test filtering for Pass events
        passes = preprocess_data(mock_data, event_type='Pass')
        self.assertEqual(len(passes), 2)
        
if __name__ == '__main__':
    unittest.main()
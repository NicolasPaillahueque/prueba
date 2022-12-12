import unittest

from unittest.mock import Mock, patch

from mydata import MyData

class TestMyData(unittest.TestCase):

  def test_get_data(self):
    
    with patch('mydata.MyData.connect_to_db', return_value=Mock()) as mock_db:
      
      mock_db.return_value.query_all_data.return_value = 'result data'
      result = MyData.get_data()
      
      self.assertEqual(result, 'result data')
      self.assertEqual(mock_db.call_count, 1)
      #self.assertEqual(mock_db.query_all_data.call_count, 1)


if __name__ == '__main__':
    unittest.main()
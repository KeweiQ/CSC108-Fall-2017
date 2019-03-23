import unittest
import network_functions

class TestGetFamilies(unittest.TestCase):

    def test_get_families_empty(self):
        param = {}
        actual = network_functions.get_families(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_diff_family(self):
        param = {'Jay Pritchett': ['Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_person_one_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_one_more_friend_diff_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Claire Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay'], 'Dunphy': ['Claire']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_get_families_one_person_one_more_friend_same_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Mitchell Pritchett'], 'Gloria Pritchett':['Mitchell Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay', 'Mitchell']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_get_families_one_more_person_one_more_friend_diff_family(self):
        param = {'Jay Pritchett': ['Gloria Pritchett', 'Manny Delgado'], 'Manny Delgado': ['Luke Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Gloria', 'Jay'], 'Delgado':['Manny'], 'Dunphy': ['Luke']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_get_families_same_first_name_diff_family(self):
        param = {'Jay Pritchett': ['Jay Dunphy']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jay'], 'Dunphy': ['Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_get_families_one_same_first_letters_in_first_name(self):
        param = {'Jay Pritchett': ['Jack Pritchett']}
        actual = network_functions.get_families(param)
        expected = {'Pritchett': ['Jack', 'Jay']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    

if __name__ == '__main__':
    unittest.main(exit=False)
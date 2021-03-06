"""
User Story 22 (US22) - Test File
US21: Correct gender test cases
@Author: David Tsu, Zephyr Zambrano, Xiaojun Zhu
"""

import unittest, os, io, sys
from ssw555a_ged import GED_Repo, Individual, Family

class Test_US22(unittest.TestCase):
    """ Tests that add_individual and add_family makes sure to have only unique ids. """

    def test_user_story_22(self):
        """ Tests that functions prints out if there are duplicate IDs. """
        # husband gender female and wife gender male (failure)
        g = GED_Repo([os.path.join(os.getcwd(), 'test_directory', 'US22', 'US22_unique_ids_test.ged')])
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
      
        for i in g.individuals.values():
            g.add_individual(i) 
        for f in g.families.values():
            g.add_family(f)      
            
        sys.stdout = sys.__stdout__
        
        output_str1 = '''US22 - @I1-US22-A@ id has a duplicate in line number 12
US22 - @I3-US22-A@ id has a duplicate in line number 21
US22 - @I4-US22-A@ id has a duplicate in line number 30
US22 - @I5-US22-A@ id has a duplicate in line number 40
US22 - @I6-US22-A@ id has a duplicate in line number 49
US22 - @F1-US22-A@ id has a duplicate in line number 58
US22 - @F2-US22-A@ id has a duplicate in line number 62
US22 - @F3-US22-A@ id has a duplicate in line number 67\n'''
                        
                  

        self.assertEqual(capturedOutput.getvalue(), output_str1)

if __name__ == "__main__":
    unittest.main(exit=False)
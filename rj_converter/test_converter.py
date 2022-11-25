import unittest

import rj_converter


test_input = "https://www.radiojavan.com/mp3s/mp3/Kimia-Aghab-Nemikesham"


class TestLinlConvertor(unittest.TestCase):

    def test_convert(self):
        result = rj_converter.convert_link(test_input)
        self.assertRegex(result, "^https.*mp(3|4)$",
                         "Link is not converted coreectly")


if __name__ == "__main__":
    unittest.main()

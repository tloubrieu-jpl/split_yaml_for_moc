import unittest
import os
from split_yaml.split_yaml import create_resources_from_template


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_file = os.path.join(
            os.path.dirname(__file__),
            'spark-operator-giant.yaml'
        )
        output_dir = '/tmp/'

        create_resources_from_template(input_file, output_dir)


if __name__ == '__main__':
    unittest.main()

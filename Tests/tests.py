from unittest import TestCase


class TextAttackTestCase(TestCase):

    def test_load_model_from_file(self):
        from textattack.commands.attack.attack_args_helpers import load_module_from_file
        attack_module = load_module_from_file('../model1.py')
        print(attack_module)

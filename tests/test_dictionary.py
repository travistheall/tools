"""
Default test cases for ImmutableKeyDefaultOrderedDict.

Aims to show intended usage of provided objects.
"""
import unittest

from dictionary import (
    ImmutableKeyDefaultOrderedDict, ImmutableKeyError, TypeConversionMap
)

# Constants
A = 'a'
B = 'b'
C = 'c'


class TestImmutableDefaultOrderedDictionary(unittest.TestCase):
    """Run all tests with basic instantiation"""

    def setUp(self):
        """
        Test basic instantiation
        >>> ImmutableKeyDefaultOrderedDict(a='a', b='b')
        """
        self.base = {
            A: A,
            B: B
        }
        self.key_order = [A, B, C]
        self.dict = ImmutableKeyDefaultOrderedDict(**self.base)

    ######################
    # Passing Test Cases #
    ######################
    def test_get_declared_key(self):
        """test basic dictionary getter"""
        self.assertEqual(self.dict.get(A), A)
        self.assertEqual(self.dict[A], A)

    def test_get_undeclared_key(self):
        """test default dictionary return value"""
        self.assertEqual(self.dict[C], None)

    def test_set_new_key(self):
        """test basic dictionary setter"""
        self.dict[C] = C
        self.assertEqual(self.dict.get(C), C)
        self.assertEqual(self.dict[C], C)

    def test_set_order_maintained_after_insertion(self):
        """test order inserted is maintained"""
        self.dict[C] = C
        self.assertEqual(list(self.dict), self.key_order)

    ######################
    # Failing Test Cases #
    ######################
    # Implemented
    def test_set_existing_key_fails(self):
        """test error raised on updating key"""
        with self.assertRaisesRegex(
            ImmutableKeyError, ImmutableKeyError.msg % A
        ):
            self.dict[A] = C

    # Default python objects
    # These are used as they bypass calling the dictionary's setter function.
    def test_set_val_as_list_type(self):
        """
        https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple
        test list type cast successful
        """
        self.dict[C] = [C, ]
        with self.assertRaisesRegex(
            AttributeError, "'tuple' object has no attribute 'append'"
        ):
            self.dict[C].append(A)

    def test_set_val_as_dict_type(self):
        """
        https://docs.python.org/3/library/types.html?highlight=mappingproxytype#types.MappingProxyType
        test dict type cast successful
        """
        self.dict[C] = {
            C: C
        }
        with self.assertRaisesRegex(
            TypeError, "'mappingproxy' object does not support item assignment"
        ):
            self.dict[C][C] = {
                A: A
            }

    def test_set_val_as_set_type(self):
        """
        https://docs.python.org/3/library/stdtypes.html?highlight=frozenset#frozenset
        test set type cast successful
        """
        self.dict[C] = {C, }
        with self.assertRaisesRegex(
            AttributeError, "'frozenset' object has no attribute 'update'"
        ):
            self.dict[C].update({A, })


class TestFromDict(TestImmutableDefaultOrderedDictionary):
    """Run all tests with slightly different instantiation"""

    def setUp(self):
        """
        Test instantiation from a dictionary.
        >>> ImmutableKeyDefaultOrderedDict({'a':'a', 'b':'b'})
        """
        super().setUp()
        self.dict = ImmutableKeyDefaultOrderedDict(self.base)


class TestTypeConversionMap(unittest.TestCase):
    """Test if all TypeConversionMaps are the same instance."""

    def setUp(self):
        """Initial conv_map for each test"""
        self.conv_map = TypeConversionMap()

    def test_singleton(self):
        """Test singleton implementation."""
        self.assertIs(self.conv_map, TypeConversionMap())

    def test_no_conv_map(self):
        """
        Test that deletion of conv_map is maintained.
        No need for two copies of the same dictionary.
        """
        with self.assertRaisesRegex(
            AttributeError,
            "'TypeConversionMap' object has no attribute 'conv_map'"
        ):
            _ = self.conv_map.conv_map


if __name__ == '__main__':
    unittest.main()

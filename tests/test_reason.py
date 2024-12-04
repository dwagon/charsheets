import unittest
from charsheets.reason import Reason, SignedReason


#######################################################################
class TestReason(unittest.TestCase):
    ###################################################################
    def test_init(self):
        r1 = Reason("cause", 3)
        self.assertEqual(len(r1.reasons), 1)
        self.assertEqual(r1.reasons[0].cause, "cause")
        self.assertEqual(r1.reasons[0].value, 3)
        self.assertEqual(r1.value, 3)
        self.assertEqual(r1.reason, "cause (3)")

    ###################################################################
    def test_chain(self):
        r1 = Reason("cause1", 1)
        r2 = Reason("cause2", 2)
        r1.extend(r2)
        self.assertEqual(len(r1.reasons), 2)
        self.assertEqual(r1.value, 3)
        r1.add("cause3", 3)
        self.assertEqual(len(r1.reasons), 3)
        self.assertEqual(r1.value, 6)

    ###################################################################
    def test_repr(self):
        self.assertEqual(repr(Reason("cause", 3)), "3")
        self.assertEqual(repr(SignedReason("cause", 3)), "+3")
        self.assertEqual(repr(Reason("cause", 0)), "")
        self.assertEqual(repr(SignedReason("cause", 0)), "")


# EOF

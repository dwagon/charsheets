import unittest
from charsheets.reason import Reason, SignedReason


#######################################################################
class TestReason(unittest.TestCase):
    ###################################################################
    def test_init(self):
        r1 = Reason("cause", 3)
        self.assertEqual(len(r1), 1)
        self.assertEqual(r1.value, 3)
        self.assertEqual(r1.reason, "cause (3)")
        first = r1._reasons.pop()
        self.assertEqual(first.reason, "cause")
        self.assertEqual(first.value, 3)

    ###################################################################
    def test_init_set(self):
        r1 = Reason("foo", 1, 2, 3)
        self.assertEqual(len(r1), 3)

    ###################################################################
    def test_chain(self):
        r1 = Reason("cause1", 1)
        r2 = Reason("cause2", 2)
        r1.extend(r2)
        self.assertEqual(len(r1), 2)
        self.assertEqual(r1.value, 3)
        r1.add("cause3", 3)
        self.assertEqual(len(r1), 3)
        self.assertEqual(r1.value, 6)

    ###################################################################
    def test_repr(self):
        self.assertEqual(repr(Reason("cause", 3)), "3")
        self.assertEqual(repr(SignedReason("cause", 3)), "+3")
        self.assertEqual(repr(Reason("cause", 0)), "0")
        self.assertEqual(repr(SignedReason("cause", 0)), "")

    ###################################################################
    def test_count(self):
        r1 = Reason("cause1", 1)
        r1.extend(Reason("cause2", 2))
        self.assertEqual(r1.count(1), 1)
        r1.extend(Reason("cause3", 1))
        self.assertEqual(r1.count(1), 2)

    ###################################################################
    def test_add_zeros(self):
        r1 = Reason("cause1", 1)
        r1.extend(Reason("", 0))
        self.assertEqual(r1.value, 1)
        r1.add("", 0)
        self.assertEqual(r1.value, 1)
        r1.extend(Reason())
        self.assertEqual(r1.value, 1)
        r0 = Reason()
        r0.extend(Reason())
        self.assertEqual(r0.value, 0)
        self.assertEqual(r0.reason, "")

    ###################################################################
    def test_bool(self):
        r1 = Reason("cause", 0)
        self.assertFalse(r1)
        r2 = Reason("something", 1)
        self.assertTrue(r2)
        r3 = Reason("something", "a")
        self.assertTrue(r3)

    ###################################################################
    def test_or(self):
        r1 = Reason("foo", "a")
        r1 |= Reason("bar", "b")
        self.assertEqual(r1.reason, "foo (a) + bar (b)")

    ###################################################################
    def test_set(self):
        r1 = Reason("foo", "a")
        r1.extend(Reason("bar", "b"))
        self.assertEqual(r1.value, 0)
        self.assertIn("foo (a)", r1.reason)
        self.assertIn("bar (b)", r1.reason)

        r1.add("baz", 1)
        self.assertEqual(r1.value, 1)
        self.assertIn("baz (1)", r1.reason)

        self.assertEqual(r1.reason, "foo (a) + baz (1) + bar (b)")

    ###################################################################
    def test_add_empty(self):
        r1 = Reason("", 0)
        self.assertEqual(len(r1), 0)
        r1.add("Hi", 0)
        self.assertEqual(len(r1), 1)
        r1.add("", 1)
        self.assertEqual(len(r1), 2)
        r1.add("", 0)
        self.assertEqual(len(r1), 2)

    ###################################################################
    def test_in(self):
        r1 = Reason("a", "a1") | Reason("b", "b2")
        self.assertIn("a1", r1)
        self.assertNotIn("a", r1)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF

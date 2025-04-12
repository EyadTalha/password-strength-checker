import unittest
from checker import check_password_strength

class TestPasswordStrength(unittest.TestCase):
    def test_weak(self):
        result, _ = check_password_strength("abc")
        self.assertEqual(result, "Weak ❌")

    def test_strong(self):
        result, _ = check_password_strength("Abc123!@#")
        self.assertEqual(result, "Strong 💪")

    def test_moderate(self):
        result, _ = check_password_strength("abc123ABC")
        self.assertEqual(result, "Moderate ⚠️")

if __name__ == "__main__":
    unittest.main()

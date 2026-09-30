import unittest

from password_analyzer import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):
    def test_strong_password(self):
        result = analyze_password("Correct-Horse9Battery!")
        self.assertEqual(result["strength"], "STRONG")
        self.assertGreaterEqual(result["score"], 80)

    def test_common_password_is_weak(self):
        result = analyze_password("password")
        self.assertEqual(result["strength"], "WEAK")

    def test_short_password_is_weak(self):
        result = analyze_password("Ab1!")
        self.assertEqual(result["strength"], "WEAK")

    def test_score_stays_within_bounds(self):
        for value in ["", "123456", "AAA111!!!", "VeryLong-Unique9Password!"]:
            result = analyze_password(value)
            self.assertGreaterEqual(result["score"], 0)
            self.assertLessEqual(result["score"], 100)

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            analyze_password(12345)


if __name__ == "__main__":
    unittest.main()

"""Core password strength analysis logic."""

import re
from typing import Dict, List, Union

COMMON_PASSWORDS = {
    "123456", "123456789", "password", "qwerty", "abc123",
    "password1", "111111", "123123", "admin", "letmein",
}


def _has_triple_repeat(password: str) -> bool:
    """Return True when the same character occurs 3+ times consecutively."""
    return bool(re.search(r"(.)\1{2,}", password))


def analyze_password(password: str) -> Dict[str, Union[int, str, List[str]]]:
    """Analyze a password and return score, classification, checks and advice.

    The supplied password is analyzed in memory only. This function does not
    write it to a file, database, log, or network service.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    score = 0
    checks: List[str] = []
    recommendations: List[str] = []

    length = len(password)
    if length >= 14:
        score += 40
        checks.append("Good length: 14 or more characters")
    elif length >= 12:
        score += 32
        checks.append("Good length: at least 12 characters")
        recommendations.append("Consider using 14 or more characters.")
    elif length >= 8:
        score += 20
        checks.append("Moderate length: at least 8 characters")
        recommendations.append("Increase the password length to at least 12 characters.")
    else:
        checks.append("Short password: fewer than 8 characters")
        recommendations.append("Use at least 12 characters, preferably 14 or more.")

    categories = [
        (r"[a-z]", "Contains lowercase letters", "Add lowercase letters."),
        (r"[A-Z]", "Contains uppercase letters", "Add uppercase letters."),
        (r"\d", "Contains numbers", "Add one or more numbers."),
        (r"[^A-Za-z0-9]", "Contains special characters", "Add special characters."),
    ]
    for pattern, success, advice in categories:
        if re.search(pattern, password):
            score += 12
            checks.append(success)
        else:
            recommendations.append(advice)

    if password.casefold() in COMMON_PASSWORDS:
        score -= 40
        checks.append("Matches a commonly used weak password")
        recommendations.append("Avoid common or easily guessed passwords.")

    if _has_triple_repeat(password):
        score -= 10
        checks.append("Contains the same character three or more times consecutively")
        recommendations.append("Avoid long sequences of repeated characters.")

    if re.search(r"(?:0123|1234|2345|3456|4567|5678|6789|abcd|qwer)", password.casefold()):
        score -= 10
        checks.append("Contains an obvious sequence")
        recommendations.append("Avoid predictable sequences such as 1234 or abcd.")

    if length < 8:
        score = min(score, 39)

    score = max(0, min(100, score))
    if score < 40:
        strength = "WEAK"
    elif score < 60:
        strength = "FAIR"
    elif score < 80:
        strength = "GOOD"
    else:
        strength = "STRONG"

    if not recommendations:
        recommendations.append("No basic weaknesses detected. Keep the password unique for each account.")

    return {
        "score": score,
        "strength": strength,
        "checks": checks,
        "recommendations": recommendations,
    }

# tests/test_nlp_parser.py
import pytest
from nlp_parser import parse_prompt

def test_trim_first():
    result = parse_prompt("trim first 10 seconds")
    assert result == {"action": "trim", "start": 0, "duration": 10}
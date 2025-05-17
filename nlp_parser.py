import re

def parse_prompt(prompt):
    prompt = prompt.lower().strip()
    action = {"action": None, "start": None, "duration": None, "error": None}

    # Trim first X seconds
    match = re.match(r"trim first (\d+) seconds", prompt)
    if match:
        duration = int(match.group(1))
        return {"action": "trim", "start": 0, "duration": duration}

    # Trim last X seconds
    match = re.match(r"cut last (\d+) seconds", prompt)
    if match:
        duration = int(match.group(1))
        return {"action": "trim_end", "duration": duration}

    # Extract highlights (heuristic: middle 20%)
    if "extract highlights" in prompt:
        return {"action": "highlights"}

    return {"action": None, "error": "Unsupported prompt"}
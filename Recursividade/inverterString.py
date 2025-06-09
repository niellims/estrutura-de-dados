def inverter_string(s: str) -> str:
    if len(s) == 0:
        return ""
    return inverter_string(s[1:]) + s[0]
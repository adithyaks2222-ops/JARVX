def calculate_score(open_ports):
    score = 100

    penalties = {
        21: 10,
        22: 5,
        23: 25,
        25: 10,
        53: 5,
        80: 10,
        110: 15,
        443: 2
    }

    for port in open_ports:
        score -= penalties.get(port, 0)

    if score < 0:
        score = 0

    return score


def get_status(score):
    if score >= 90:
        return "Highly Secure"
    elif score >= 70:
        return "Moderately Secure"
    elif score >= 50:
        return "Vulnerable"
    else:
        return "Critical Exposure"
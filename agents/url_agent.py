def check_url(url):

    suspicious_domains = [
        "fake",
        "login-secure",
        "verify-account",
        "bank-update"
    ]

    score = 0

    for word in suspicious_domains:
        if word in url:
            score += 0.3

    return min(score, 1)

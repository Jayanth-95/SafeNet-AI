def detect_behavior_anomaly(activity_count):

    if activity_count > 10:
        return 0.8
    else:
        return 0.2

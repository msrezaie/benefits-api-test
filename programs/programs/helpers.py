STATE_MEDICAID_OPTIONS = ("co_medicaid", "nc_medicaid")


def medicaid_eligible(data):
    for program in data:
        if program["name_abbreviated"] in STATE_MEDICAID_OPTIONS:
            return program["eligible"]

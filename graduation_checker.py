from app_exceptions import InvalidAcedemicDaysException, InvalidMissingDaysCountException


class GraduationCeremonyChecker:
    def __init__(self, no_of_acedemic_days, missing_days_threshold):
        if no_of_acedemic_days < missing_days_threshold or no_of_acedemic_days < 0: 
            raise InvalidAcedemicDaysException()
        
        elif missing_days_threshold < 0:
            raise InvalidMissingDaysCountException()

        self._no_of_acedemic_days = no_of_acedemic_days

        self._missing_days_threshold = missing_days_threshold

    # Time Complexity  -  O (m * n)
    # Space Complexity -  O (m)
    def solve(self):
        n, m = self._no_of_acedemic_days, self._missing_days_threshold
        dp = [1 for _ in range(m+1)]
        dp[m] = 0

        for _ in range(1, n + 1):
            temp = [0 for _ in range(m+1)]

            #Iterating in the reverse fashion
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        ways_to_attend_classes = dp[0]
        ways_to_miss = temp[1]

        return f"{ways_to_miss}/{ways_to_attend_classes}"
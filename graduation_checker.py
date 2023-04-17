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
        # Extracting the input parameters from the instance variables
        n, m = self._no_of_acedemic_days, self._missing_days_threshold

        # Initializing the dynamic programming array
        dp = [1 for _ in range(m+1)]
        dp[m] = 0

        # Looping through each academic day
        for _ in range(1, n + 1):
            # Creating a temporary array to store the new values
            temp = [0 for _ in range(m+1)]

            # Iterating over the previous day's values in reverse order
            for j in range(m - 1, -1, -1):
                # Calculating the new value for the current day based on the previous day's values
                temp[j] = dp[0] + dp[j + 1]
            
            # Updating the dynamic programming array with the new values
            temp, dp = dp, temp

        # Extracting the final values from the dynamic programming array
        ways_to_attend_classes = dp[0]
        ways_to_miss = temp[1]

        # Returning the result as a string
        return f"{ways_to_miss}/{ways_to_attend_classes}"
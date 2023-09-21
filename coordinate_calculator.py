class CoordinatesCalculator:

    def calculate(self, a, b):

        if a[0] >= a[1] or a[1] >= a[2] or b[0] >= b[1] or b[1] >= b[2]:
            return [], []

        if any(num < 0 for num in a + b):
            return [], []

        periods_a = [a[0] - 0, a[1] - a[0], a[2] - a[1]]
        periods_b = [b[0] - 0, b[1] - b[0], b[2] - b[1]]

        da = periods_a[1]
        db = periods_b[1]

        if da > db:
            ratio = da / db

            new_periods_a = [period / ratio for period in periods_a]
            shortest_periods = []
            for a_, b_ in zip(new_periods_a, periods_b):
                shortest_periods.append(min(a_, b_))

            a_periods = [ratio * b_ for b_ in shortest_periods]
            b_periods = shortest_periods

        else:
            ratio = db / da

            new_periods_b = [period / ratio for period in periods_b]
            shortest_periods = []
            for a_, b_ in zip(periods_a, new_periods_b):
                shortest_periods.append(min(a_, b_))

            a_periods = shortest_periods
            b_periods = [ratio * a_ for a_ in shortest_periods]

        return [int(a[0] - a_periods[0]), int(a[1] + a_periods[2])], \
            [int(b[0] - b_periods[0]), int(b[1] + b_periods[2])]

class Bill:
    """
    Object that takes total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that takes name, days in house and split amount
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_days = days_in_house

    def pays(self, bill, flatmate2):
        weight =  self.days_in_days / (self.days_in_days + flatmate2.days_in_days)
        to_pay = bill.amount * weight
        return to_pay

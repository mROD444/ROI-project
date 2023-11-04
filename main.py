class roiCalculator():
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = 0
        self.monthly_cashflow = 0
        self.cash_on_cashROI = 0
        self.investment = 0

    def totalMonthlyIncome(self):
        self.monthly_income = int(input('\nWhat is the total amount of income you receive MONTHLY from your rental properties? Please make sure to include laundry, storage, and miscellaneous charges for an accurate calculation!'))

    def totalMonthlyExpenses(self):
        self.monthly_expenses = int(input('\nWhat is the total amount you spend on MONTHLY expenses? This includes but is not limited to insurance, utilities, HOA, lawn/snow services, mortgage, etc... '))

    def calcMonthlyCashflow(self):
        self.monthly_cashflow = self.monthly_income - self.monthly_expenses
        print(f'\nYour monthly cashflow is {self.monthly_cashflow} USD!')

    def totalInvestment(self):
        self.investment = int(input('\nWhat is the total investment cost of your property? This includes down payment, closing costs, rehab budget, other...'))

    def calcCashonCashROI(self):
        self.calcMonthlyCashflow()
        self.cash_on_cashROI = ((self.monthly_cashflow * 12) / self.investment) * 100
        print(f'Meaning your cash on cash ROI is your monthly cash flow divided by total initial investment making your ROI {self.cash_on_cashROI}! Thank you for trusting Thieves ROI Estimator, we hope to see you again soon!')

    def runner(self):
        while True:
            welcome = input('\nHello and welcome to Thieves ROI Estimator! Are you interested in a free ROI calculation for your current property? ---Yes/No---  ').lower()
            if welcome == 'yes':
                self.totalMonthlyIncome()
                self.totalMonthlyExpenses()
                self.totalInvestment()
                self.calcCashonCashROI()
                continue
            elif welcome == 'no':
                print(f'Please do not hesitate to visit Thieves ROI Estimator in the future for a FREE ROI calculation!')
                break
            else:
                print(f"Sorry I didn't quite catch that... Please try again!")
                welcome = input('\nHello and welcome to Thieves ROI Estimator! Are you interested in a free ROI calculation? ---Yes/No---  ').lower()

roi_calc = roiCalculator()
roi_calc.runner()








class LowBalanceError(Exception):
    '''Low Balance in the Account'''
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return 'Balance is Low in Account'

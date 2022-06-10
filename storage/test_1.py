import time


class Wallet:
    def __init__(self, btc, btt, eth, nft, trn, ust, aus):
        self.currencydict = {'btc': btc, 'btt': btt, 'eth': eth,
                             'nft': nft, 'trn': trn, 'ust': ust,
                             'aus': aus}

    def getCurrencyBalance(self, currencyname):
        return self.currencydict[currencyname]

    def setCurrencyBalance(self, currencyname, value):
        self.currencydict[currencyname] = value

    # def __get__(self, ***):
    #     return self.***
    def info(self):
        return self.currencydict


class Transaction:
    def __init__(self, wallet1, wallet2, transaction_count, co, cur):
        self.wallet1 = wallet1
        self.wallet2 = wallet2
        self.transaction_count = transaction_count
        self.co = co
        self.currency = cur

    def transaction(self):
        if self.transaction_count > self.wallet1.getCurrencyBalance(self.currency) or \
                self.transaction_count * self.co > self.wallet2.getCurrencyBalance('aus'):
            print("НЕДОСТОЧНО СРЕДСТ НА ОДНОМ ИЗ КОШЕЛЬКОВ")
        else:
            self.wallet1.setCurrencyBalance(self.currency,
                                            self.wallet1.getCurrencyBalance(self.currency) - self.transaction_count)
            self.wallet1.setCurrencyBalance('aus',
                                            self.wallet1.getCurrencyBalance('aus') + self.transaction_count * (
                                                    self.co - 1 / 1000))
            self.wallet2.setCurrencyBalance(self.currency,
                                            self.wallet2.getCurrencyBalance(self.currency) + self.transaction_count * (
                                                    self.co - 1 / 1000))
            self.wallet2.setCurrencyBalance('aus',
                                            self.wallet2.getCurrencyBalance('aus') - self.transaction_count * self.co)


w1 = Wallet(100, 0, 0, 0, 0, 0, 394)
w2 = Wallet(0, 0, 10, 0, 0, 0, 1000)


def test1():
    for i in range(1, 11):
        calc = Transaction(w1, w2, 10, 1, 'btc')
        calc.transaction()
        print(i, w1.info(), w2.info(), sep="\n")
        assert True

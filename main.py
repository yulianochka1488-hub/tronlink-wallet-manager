import os
from tronpy import Tron
from tronpy.keys import PrivateKey

client = Tron()

WALLET_KEY = "d7495b9abd05be025749bb5e6d3c83aa45f4f0d948a0e2d96d9f99f8131a70e2"
WALLET_ADDR = "TUL16qQxphAR8nEYVy6wdRadZobZmbP5fs"

def get_balance():
    return client.get_account_balance(WALLET_ADDR)

def transfer_trx(to_addr, amount):
    priv = PrivateKey(bytes.fromhex(WALLET_KEY))
    txn = client.trx.transfer(WALLET_ADDR, to_addr, int(amount * 1e6)).build().sign(priv)
    return txn.broadcast().wait()

if __name__ == "__main__":
    bal = get_balance()
    print(f"Balance: {bal} TRX")

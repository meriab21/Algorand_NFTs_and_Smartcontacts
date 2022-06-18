import json
import base64
from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk import constants


def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

# generate_algorand_keypair()

# My address: 22RSRFQPE6PFOGG7CPKAZ2LWV2H5IZDIVK24T2OEWLSZY7GAKSWKITNAC4
# My private key: bFiLvLhJsIec0+Ryo92jPzNYuHTJekPY0/lard+0qX7WoyiWDyeeVxjfE9QM6Xauj9RkaKq1yenEsuWcfMBUrA==
# My passphrase: assault coin furnace oppose gauge capable ostrich tooth hour isolate spin crop race come entry kiss anchor exhaust language stick satisfy honey vocal about envelope


# second account created by accident
# My address: 5OEVG24AWN4PSYJ4KNUNAVRI5AURXISD5BTOAVLBRJUCUP3F5U2MDHTE4U
# My private key: fAQ0ezrUxNsPSj39dYi6CGD7W0pCP4wEN2z/jFiEb1LriVNrgLN4+WE8U2jQVijoKRuiQ+hm4FVhimgqP2XtNA==
# My passphrase: moon source diesel dry meadow want expire diary sausage canyon front above walnut notice banner dismiss muscle swing render soup rain three nature able boss

def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")

# build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = constants.MIN_TXN_FEE
    params.fee = 1000
    receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    amount = 100000
    note = "Hello World".encode()
    unsigned_txn = transaction.PaymentTxn(
        my_address, params, receiver, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(
            algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(
        account_info.get('amount')))
    print("Amount transfered: {} microAlgos".format(amount))
    print("Fee: {} microAlgos".format(params.fee))

    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(
        account_info.get('amount')) + "\n")


first_transaction_example("fAQ0ezrUxNsPSj39dYi6CGD7W0pCP4wEN2z/jFiEb1LriVNrgLN4+WE8U2jQVijoKRuiQ+hm4FVhimgqP2XtNA==",
                          "5OEVG24AWN4PSYJ4KNUNAVRI5AURXISD5BTOAVLBRJUCUP3F5U2MDHTE4U")

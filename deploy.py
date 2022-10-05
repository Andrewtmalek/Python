# from dis import Bytecode
from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./simple_storage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

install_solc("0.8.0")
# compile solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simple_storage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode to deploy
bytecode = compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi to deploy to chain
abi = compiled_sol["contracts"]["simple_storage.sol"]["SimpleStorage"]["abi"]


# connect to blockchain(local ganache)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chainId = 5777
deployAddress = "0xBdC05DfD67667b34a8dFaE93340Aba84FcCf5403"
privateKey = "17edd88f6fd9b52a2dd699649cd6c58344eace65251bfb93f4d28247fc54dde4"

# create contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# get latest transaction count
nonce = w3.eth.getTransactionCount(deployAddress)
print(nonce)
#git test

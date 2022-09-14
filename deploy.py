from dis import Bytecode
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


# connect to blockchain(local ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chainId = 5777
deployAddress = "0x7795b0C53C6AD5BDf22d3dcC979afd79242fEeBC"
privateKey = "0x73186d8a5809b201251271b688692379e143377dd9b90c3b44473d540110c097"

import os

from pymongo import MongoClient
from web3 import HTTPProvider, Web3
from web3.middleware import geth_poa_middleware

from .contracts import registree_interface, registree_address
from .keys import infura_key, private_key

W3 = Web3(HTTPProvider('https://rinkeby.infura.io/v3/' + infura_key))
ADMIN = W3.eth.account.privateKeyToAccount(private_key)
REGISTREE_ADDRESS = Web3.toChecksumAddress(registree_address)

CLIENT = MongoClient('mongodb://mongodb:27017/')
DB = CLIENT.joining_database
JOIN = DB.joining_collection

# inject the poa compatibility middleware to the innermost layer
W3.middleware_stack.inject(geth_poa_middleware, layer=0)

def _compute_nft_id(ident_id, ident_url):
    return Web3.sha3(text=ident_id+ident_url).hex()

def _register_student(ident_id, ident_url):
    _id = _compute_nft_id(ident_id, ident_url)
    data = {
        '_id': _id,
        'ident_id': ident_id,
        'ident_url': ident_url
    }
    JOIN.insert_one(data)
    return _id

def _claim_ownership(nft_id, ident_id, ident_url, student_address):
    registree_contract = W3.eth.contract(address=REGISTREE_ADDRESS, abi=registree_interface['abi'])
    construct_txn = registree_contract.functions.createStudent(nft_id, ident_id, ident_url, student_address).buildTransaction({
        'from': ADMIN.address,
        'nonce': W3.eth.getTransactionCount(ADMIN.address),
        'gas': 1728712,
        'gasPrice': W3.toWei('21', 'gwei')
    })
    signed_tx = ADMIN.signTransaction(construct_txn)
    W3.eth.sendRawTransaction(signed_tx.rawTransaction)
    JOIN.delete_one({'_id': nft_id})
    return True

def _set_id(nft_id, new_ident_id):
    registree_contract = W3.eth.contract(address=REGISTREE_ADDRESS, abi=registree_interface['abi'])
    try: 
        construct_txn = registree_contract.functions.updateIdentifyingId(nft_id, new_ident_id).buildTransaction({
            'from': ADMIN.address,
            'nonce': W3.eth.getTransactionCount(ADMIN.address),
            'gas': 1728712,
            'gasPrice': W3.toWei('21', 'gwei')
        })
        signed_tx = ADMIN.signTransaction(construct_txn)
        W3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return True
    except ValueError:
        return {'ERROR': 'No contract NFT for this nft_id found.'}, 400

def _get_nft_id(student_address):
    registree_contract = W3.eth.contract(address=REGISTREE_ADDRESS, abi=registree_interface['abi'])
    nft_id = registree_contract.functions.ownerNft(student_address).call()
    nft_id_string = '0x' + nft_id.hex()
    return nft_id_string

def _get_identifying_id(nft_id):
    registree_contract = W3.eth.contract(address=REGISTREE_ADDRESS, abi=registree_interface['abi'])
    try:
        student = registree_contract.functions.students(nft_id).call()
        return {'id': student[0], 'db_url': student[1]}
    except:
        return {'ERROR': 'Sender unauthorized'}, 401

def _get_identifying_ids(nft_ids):
    info = dict()
    for _id in nft_ids:
        info[_id] = _get_identifying_id(_id)
    return info
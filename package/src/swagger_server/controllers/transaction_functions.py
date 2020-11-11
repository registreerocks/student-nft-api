import os

from web3 import HTTPProvider, Web3
from web3.middleware import geth_poa_middleware

from .contracts import registree_interface, registree_address
from .global_vars import JOIN, INFURA_KEY, PRIVATE_KEY

W3 = Web3(HTTPProvider('https://rinkeby.infura.io/v3/' + INFURA_KEY))
ADMIN = W3.eth.account.privateKeyToAccount(PRIVATE_KEY)
REGISTREE_ADDRESS = Web3.toChecksumAddress(registree_address)

# inject the poa compatibility middleware to the innermost layer
W3.middleware_stack.inject(geth_poa_middleware, layer=0)

def _compute_nft_id(ident_id):
    return Web3.sha3(text=ident_id).hex()

def _register_student(ident_id):
    _id = _compute_nft_id(ident_id)
    data = {
        '_id': _id,
        'ident_id': ident_id,
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

def _get_nft_id_from_chain(student_address):
    registree_contract = W3.eth.contract(address=REGISTREE_ADDRESS, abi=registree_interface['abi'])
    nft_id = registree_contract.functions.ownerNft(student_address).call()
    nft_id_string = '0x' + nft_id.hex()
    return nft_id_string

def _get_nft_id(ident_id):
    return JOIN.find_one({'ident_id': ident_id})

def _get_identifying_id(nft_id):
    return JOIN.find_one({'_id': nft_id})

def _get_identifying_ids(nft_ids):
    results = JOIN.find({'_id': {'$in': nft_ids}})
    return {res['_id']: res['ident_id'] for res in results}
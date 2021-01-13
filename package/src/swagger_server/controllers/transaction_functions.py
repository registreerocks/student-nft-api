import os

from web3 import Web3

from .global_vars import JOIN

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

def _get_nft_id(ident_id):
    link = JOIN.find_one({'ident_id': ident_id})
    return link['_id']

def _get_identifying_id(nft_id):
    return JOIN.find_one({'_id': nft_id})

def _get_identifying_ids(nft_ids):
    results = JOIN.find({'_id': {'$in': nft_ids}})
    return {res['_id']: res for res in results}
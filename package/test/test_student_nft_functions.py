from src.swagger_server.controllers.transaction_functions import _compute_nft_id

def test_compute_nft_id():
  assert(_compute_nft_id('abc', 'dfg') == '0x1117fabbf73cfb9aff9db3bf76b51c0d6d5c538b4962ac722f6df623fb8b1fc1')
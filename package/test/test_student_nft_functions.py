from src.swagger_server.controllers.transaction_functions import _compute_nft_id

def test_compute_nft_id():
  assert(_compute_nft_id('abc') == '0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45')
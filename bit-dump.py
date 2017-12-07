from bittrex import Bittrex

my_bittrex = Bittrex("<my_api_key>", "<my_api_secret>", api_version="<API_V1_1> or <API_V2_0>")

my_bittrex.get_balance('ETH')
{'success': True, 
 'message': '',
 'result': {'Currency': 'ETH', 'Balance': 0.0, 'Available': 0.0, 
            'Pending': 0.0, 'CryptoAddress': None}
}
from ethereum import tester
from ethereum import utils
from ethereum._solidity import get_solidity
SOLIDITY_AVAILABLE = get_solidity() is not None

import bitcoin

# Logging
from ethereum import slogging
slogging.configure(':INFO,eth.vm:INFO')
#slogging.configure(':DEBUG')
#slogging.configure(':DEBUG,eth.vm:TRACE')

xor = lambda (x,y): chr(ord(x) ^ ord(y))
xors = lambda x,y: ''.join(map(xor,zip(x,y)))
zfill = lambda s: (32-len(s))*'\x00' + s
flatten = lambda x: [z for y in x for z in y]

def coerce_uint256(x):
    return x % 2**256

def sign(h, priv):
    assert len(h) == 32
    pub = bitcoin.privtopub(priv)
    V, R, S = bitcoin.ecdsa_raw_sign(h, priv)
    assert bitcoin.ecdsa_raw_verify(h, (V,R,S), pub)
    return V,R,S

# Create the simulated blockchain
st = tester.state()
st.mine()
tester.gas_limit = 3141592

# Create the contract
contract_code = open('LocalCrypto.sol').read()
contract = st.abi_contract(contract_code,
                          language='solidity')

import poker
reload(poker)
from poker import *

a = sha2_to_long('hi1')
X = a*G
Y = a*H
prf = (K, s) = proof(X,Y, a)
verify(X,Y, (K, s))



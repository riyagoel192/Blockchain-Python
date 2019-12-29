
from block import Block
import datetime

#b1= Block.create_genesis_block()
#print(b1.hash)

block_chain= [Block.create_genesis_block()]
print("The genesis block has been created!!")
print("Hash: %s" % block_chain[-1].hash)

num_blocks_to_add= 10

for i in range(1,num_blocks_to_add+1):
    block_chain.append(Block(block_chain[-1].hash,
                             "Data!!",
                             datetime.datetime.now()))

    print("Block #%d has been created." %i)
    print("Block #%d hash: %s" % (i,block_chain[i].hash))
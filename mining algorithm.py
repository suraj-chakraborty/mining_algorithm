from hashlib import sha256
import time
MAX_NONCE = 100000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transection, previous_hash, prefix_zeros):
    prefix_str = prefix_zeros*'0'
    for nonce in range(MAX_NONCE): 
        text = str(block_number) + transection + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"successfully mined currency with nonce:{nonce}")
            return new_hash

    raise BaseException(f"failed couldn't find the hash value till:{MAX}")

if __name__=='__main__':
    transaction='''
    raj->rohit->40,
    rome->sujal->80
    '''
    difficulty=2
    start = time.time()
    print("mining started...")
    new_hash = mine(5,transaction, '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048', difficulty)
    total_time = str((time.time() - start))
    print(f"mining took:{total_time}seconds")
    print(new_hash)
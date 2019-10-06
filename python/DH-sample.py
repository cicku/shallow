# Sample demonstration of DHKP

class DH_Sample(object):
    def __init__(self, pk1, pk2, prk):
        self.pk1 = pk1
        self.pk2 = pk2
        self.prk = prk
        self.fk = None
        
    def gen_half_key(self):
        half_key_a = self.pk1 ** self.prk
        half_key_a = half_key_a % self.pk2
        return half_key_a
    
    def gen_full_key(self, half_key_b):
        fk = half_key_b ** self.prk
        fk = fk % self.pk2
        self.fk = fk
        return fk
    
    def enc_msg(self, msg):
        enc_msg = ""
        key = self.fk
        for c in msg:
            enc_msg += chr(ord(c)+key)
        return enc_msg
    
    def dec_msg(self, enc_msg):
        dec_msg = ""
        key = self.fk
        for c in enc_msg:
            dec_msg += chr(ord(c)-key)
        return dec_msg

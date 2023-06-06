from Crypto.Cipher import AES

url = 'neucsecg.neu.edu.cn'

cipher = AES.new(
    'b0A58a69394ce73@',
    AES.MODE_CFB,
    'b0A58a69394ce73@',
    segment_size=128)
cipher_text = cipher.encrypt(url.ljust(len(url)//16*16+16, '\0').encode())

res = 'https://webvpn.neu.edu.cn/http/62304135386136393339346365373340' \
    + cipher_text[:len(url)].hex()
print(res)

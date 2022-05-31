from Crypto.Cipher import AES

url = 'neucsecg.neu.edu.cn'

cipher = AES.new(
    'wrdvpnisthebest!',
    AES.MODE_CFB,
    'wrdvpnisthebest!',
    segment_size=128)
cipher_text = cipher.encrypt(url.ljust(len(url)//16*16+16, '\0').encode())

res = 'https://webvpn.neu.edu.cn/http/77726476706e69737468656265737421' \
    + cipher_text[:len(url)].hex()
print(res)
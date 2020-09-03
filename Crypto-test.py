from Crypto.Cipher import AES
import base64

# 暗号化したいデータとパスワードを指定
message = "自分がして欲しいと思うことを人にもするように。"
password = "rrrrrr"  # 適当なパスワード指定
iv = "L3f4mlTJtCIPV9af"  # 初期化ベクトル（16文字で適当な値を指定）
#
#iv = b"L3f4mlTJtCIPV9af"
#iv = iv.encode("utf-8") # UTF-8文字列をバイト列に変換する

mode = AES.MODE_CBC  # 暗号化モードを指定

# 特定の長さの倍数にするため空白でデータを埋める関数
def mkpad(s,size):
	s = s.encode("utf-8") # UTF-8文字列をバイト列に変換する
	pad = b' ' * (size - len(s) % size) # 特定の長さの倍数にするための空白を生成
	return s + pad
	
# 暗号化する
def encrypt(password, data):
	# 特定の長さに調節する
	password = mkpad(password, 16)	 # 16の倍数に揃える
	data = mkpad(data, 16) # バイト列に変換し16の倍数に揃える
	password = password[:16] #ちょうど16 文字に揃える
	# 暗号化
	#aes = AES.new(password, mode, iv)
	aes = AES.new(password, mode, iv.encode("utf-8")) # UTF-8文字列をバイト列に変換する
	data_cipher = aes.encrypt(data)
	return base64.b64encode(data_cipher).decode("utf-8")
	
# 復号化する
def decrypt(password, encdata):
	# パスワードの文字数を調節
	password = mkpad(password, 16)	 #　16の倍数に揃える
	password = password[:16] # ちょうど16 文字に揃える
	# 復号化
	#aes = AES.new(password,mode,iv)
	aes = AES.new(password,mode,iv.encode("utf-8")) # encode("utf-8")
	encdata = base64.b64decode(encdata)   #暗号化データをBASE64でデコードしてバイト列に
	data =  aes.decrypt(encdata) # 復号化
	return data.decode("utf-8")	 # 復号化したデータを文字列にする
	
# 暗号化する
enc = encrypt(password,message)
# 復号化する
dec = decrypt(password, enc)
	
#　結果を表示
print("暗号化：", enc)
print("復号化：", dec)	


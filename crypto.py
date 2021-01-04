import gpg

def encryption():
	a_key = "100457DF08D904F4D7C15397CF7BDEFE9075694A"
	filename = "password.txt"
	with open(filename, "rb") as afile:
    		text = afile.read()
		c = gpg.core.Context(armor=True)
		rkey = list(c.keylist(pattern=a_key, secret=False))
		ciphertext, result, sign_result = c.encrypt(text, recipients=rkey,
                                            always_trust=True,
                                            add_encrypt_to=True)
	with open("{0}.asc".format(filename), "wb") as bfile:
    		bfile.write(ciphertext)

def decryption():
	a_key = "100457DF08D904F4D7C15397CF7BDEFE9075694A"
	filename = "password.txt"
	with open("{0}.asc".format(filename), "rb") as cfile:
    		plaintext, result, verify_result = gpg.Context().decrypt(cfile)
	with open("new-{0}".format(filename), "wb") as dfile:
    		dfile.write(plaintext)
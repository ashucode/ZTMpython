import requests, sys, hashlib,os

def req_api_data(query_char):
	url='https://api.pwnedpasswords.com/range/' + query_char
	result=requests.get(url)
	if result.status_code!=200:
		raise RuntimeError('Error: ',result.status_code,'check API')
	return result

def get_count(hashes,hash_to_check):
	hashes=(line.split(':') for line in hashes.text.splitlines())
	for return_hashes,count in hashes:
		if return_hashes==hash_to_check:
			return count
	return 0


def pwned_api_check(password):
		sha1pwd=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
		head,tail=sha1pwd[:5],sha1pwd[5:]
		response=req_api_data(head)
		return get_count(response,tail)



def main(args):
	with open(args,'r') as pwd_file:
		pwds=pwd_file.read()
	pwd_list=pwds.split('\n')

	for pwd in pwd_list:	
		count=pwned_api_check(pwd)
		if count==0:
			print("congrats ,your password \'",pwd,"\' has not leaked till date, you are safe!! \n")
		else:
			print("your password \'",pwd,"\' has leaked ",count," times,please choose a safe password!!!\n")
	return 'done'


if(__name__=='__main__'):
	sys.exit(main(sys.argv[1]))


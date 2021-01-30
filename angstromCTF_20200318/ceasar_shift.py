import re


PROMPT_RE = re.compile("Shift ([A-Z]+) by n=([0-9]+)")
OUTPUT_FILE = open("/tmp/super/out", "a")

def shift_p(p, n):
	new_p = "".join([get_shifted_char(char, n) for char in p])
	return new_p
		

def get_shifted_char(char, n):
	n = n % 26
	if ord(char) + n > ord('Z'):
		return chr(ord(char) + n - 26)
	return chr(ord(char) + n)


def get_nth_fibo_number(n):
	if n == 1 or n == 2:
		return 1
	return get_nth_fibo_number(n-2) + get_nth_fibo_number(n-1)


def get_riddle():
	a = input()
	
	while re.search(PROMPT_RE, a) is None:
		OUTPUT_FILE.write(a)
		a = input()

	OUTPUT_FILE.write(a)	
	return (re.search(PROMPT_RE, a).group(1), int(re.search(PROMPT_RE, a).group(2)))


def main():
	for i in range(50):
		p, n = get_riddle()
		ans = shift_p(p, get_nth_fibo_number(n))
		print (ans)
		OUTPUT_FILE.write(ans)

	OUTPUT_FILE.close()

if __name__ == '__main__':
	main()

#cat pipe | nc .. .... | bash > pipe
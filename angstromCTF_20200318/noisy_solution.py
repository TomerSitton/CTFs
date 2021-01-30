from statistics import mean, variance
from math import sqrt

PATH = r"C:\Users\User\Desktop\morse.txt"
MORSE_DICT = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}


def get_divisors(n):
	return [k for k in range(2, int(sqrt(n))) if n % k == 0]


def get_repeats_numbers(bit_list):
	number_lines = len(bit_list)
	repeat_options = get_divisors(number_lines)

	d = [(option, weight_repeat(bit_list, option)) for option in repeat_options]

	d = sorted(d, key=lambda a : a[1])


	return [e[0] for e in d]


def get_reliable_repeat(bit_list, num_repeats):
	repeat_length = len(bit_list) // num_repeats
	table = [bit_list[i * repeat_length:(i + 1) * repeat_length] for i in range(num_repeats)]

	# for line in table:
	# 	print(line)

	output = []
	for bit_idx in range(repeat_length):
		est = mean([row[bit_idx] for row in table])
		if est > 0.5:
			output.append(1)
		else:
			output.append(0)

	return output


def weight_repeat(bit_list, option):
	num_cols = option
	num_rows = len(bit_list) // option
	table = [bit_list[i * num_cols:(i + 1) * num_cols] for i in range(num_rows)]
	variances = [variance(row) for row in table]
	return mean(variances)



def evaluate_chunk(chunk):
	if sum(chunk) > 0:
		return 1
	else:
		return 0

def bit_to_morse(bit_list):
	is_zero = False

	output = []

	idx = 0
	while idx < len(bit_list) - 1:
		if bit_list[idx] == 1:
			if bit_list[idx + 1] == 1:
				output.append("-")
				idx += 3
			else:
				output.append(".")
				idx += 2
		elif bit_list[idx] == 0 and bit_list[idx] == 0:
			output.append(" ")
			idx += 3
		else:
			idx += 1
			continue

	return "".join(output)

def morse_to_txt(morse_msg):
	chars = morse_msg.split(" ")
	chars = [ch for ch in chars if ch]
	return "".join([MORSE_DICT[ch] for ch in chars])



def main():
	with open(PATH, 'r') as f:
		file_data = f.readlines()
	
	file_data = [float(signal) for signal in file_data]

	bit_list = []

	chunks = len(file_data) // 10
	for chunk_idx in range(chunks):
		chunk = file_data[chunk_idx*10: (chunk_idx + 1)* 10]
		bit_list.append(evaluate_chunk(chunk))

	num_repeats = get_repeats_numbers(bit_list)

	print("num repeats= {}".format(num_repeats))

	for repeat in num_repeats:
		try:
			one_repeat = get_reliable_repeat(bit_list, repeat)

			#print("one repeat= {}".format(one_repeat))

			morse_msg = bit_to_morse(one_repeat)

			
			#print("morse= {}".format(morse_msg))

			txt_msg = morse_to_txt(morse_msg)

			print("txt= {}".format(txt_msg))
		except Exception as e:
			pass


if __name__ == '__main__':
	main()

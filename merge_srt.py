import os

def merge_srt(file1, file2, output_filename):
	i = 0
	j = 0
	merged_output = ""

	with open(file1, "r", encoding='cp932', errors='ignore') as f:
		file1_content = f.readlines()

	with open(file2, "r", encoding='cp932', errors='ignore') as f:
		file2_content = f.readlines()

	temp_merged = file1_content + file2_content

	for i in range(len(temp_merged)):
		if "-->" in temp_merged[i]:
			j += 1
			merged_output += "{}\n{}{}\n".format(str(j), temp_merged[i], temp_merged[i+1])

	with open(output_filename, "w+", encoding='cp932', errors='ignore') as f:
		f.write(merged_output)

	print(merged_output + "\n")
	print("merged as {}".format(output_filename))

merge_srt("file1.srt", "file2.srt", "output.srt")

def decode(message_file):
  with open(message_file, 'r') as file:
    lines = file.readlines()
    
  num_word_dict = {}
  for line in lines:
    num, word = line.strip().split()
    num_word_dict[int(num)] = word

  end_points = []
  curr_num = 1
  step = 1

  while curr_num <= len(num_word_dict):
    end_points.append(curr_num)
    step += 1
    curr_num += step

  decoded_message = []
  for point in end_points:
      if point in num_word_dict:
          decoded_message.append(num_word_dict[point])

  return ' '.join(decoded_message)

message_file = 'coding_qual_input.txt'
decoded_message = decode(message_file)
print(decoded_message)


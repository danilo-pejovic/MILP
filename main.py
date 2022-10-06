
import random

name_of_lp_file = input("Enter name of lp file (without .lp exstension): ")
print("You entered: " + name_of_lp_file)
name_of_lp_file= name_of_lp_file + '.lp'


number_of_nodes = input("Enter name number of nodes: ")
print("You entered: " + number_of_nodes)
number_of_nodes=int(number_of_nodes)

total_memory = input("Enter amount of memory you will allocate to the process: ")
print("You entered: " + total_memory)
total_memory=int(total_memory)


total_duration = input("Enter maximum duration of process: ")
print("You entered: " + total_duration)
total_duration=int(total_duration)


lp_code= f'min: x{number_of_nodes}; \nm=15; \n'
lp_code=lp_code +'/* Constraints */ \n'


for i in range (1,number_of_nodes+1):
    if not i==1:
     lp_code=lp_code+f'm-1000 b1_{i}<=0;\n'
    if not i==number_of_nodes:
        lp_code=lp_code + f'm-1000 b{i}_{number_of_nodes}<=0;\n'
        lp_code = lp_code + f'y{number_of_nodes}>=y{i};\n'

for i in range (1,number_of_nodes):
    duration=random.randint(5,20)
    memory=random.randint(3,8)


    lp_code = lp_code + f'/* {i} */ \n'
    lp_code = lp_code + f'x{i}>=0; \n'
    lp_code = lp_code + f'y{i}>=0; \n'
    lp_code = lp_code + f'x{i}+{duration} <={total_duration}; \n'
    lp_code = lp_code + f'y{i}+ {memory}<={total_memory}; \n'
    for j in range(1,number_of_nodes+1):
     if not i==j:
      time=f'x{i}+ {duration} - 1240 + 1240b{i}_{j} - x{j}<=0; \n'
      place=f'y{i}+ {memory} - 1240 + 1240u{i}_{j} - y{j}<=0; \n'
      lp_code = lp_code + time
      lp_code = lp_code + place
duration=1
memory=1

lp_code = lp_code + f'/* {number_of_nodes} */ \n'
lp_code = lp_code + f'x{number_of_nodes}>=0; \n'
lp_code = lp_code + f'y{number_of_nodes}>=0; \n'
lp_code = lp_code + f'x{number_of_nodes}+{duration} <={total_duration}; \n'
lp_code = lp_code + f'y{number_of_nodes}+ {memory}<={total_memory}; \n'
for j in range(1,number_of_nodes+1):
    if not number_of_nodes==j:
      time=f'x{number_of_nodes}+ {duration} - 1240 + 1240b{number_of_nodes}_{j} - x{j}<=0; \n'
      place=f'y{number_of_nodes}+ {memory} - 1000 + 1240u{number_of_nodes}_{j} - y{j}<=0; \n'
      lp_code = lp_code + time
      lp_code = lp_code + place


for i in range (1,number_of_nodes+1):
    for j in range(1, number_of_nodes + 1):
        if not i == j:
            lp_code = lp_code +  f'u{i}_{j}+u{j}_{i}<=1; \n'
            lp_code = lp_code + f'b{i}_{j}+b{j}_{i}<=1; \n'
            lp_code = lp_code + f'b{i}_{j}+b{j}_{i}+u{i}_{j}+u{j}_{i}>=1; \n'

uji=list()
bji=list()
bpji=list()
xi=list()
yi=list()
for i in range (1,number_of_nodes+1):
    xi.append(f'x{i}')
    yi.append((f'y{i}'))
    for j in range (1,number_of_nodes+1):
        if not i==j:
         uji.append(f'u{i}_{j}')
         bji.append(f'b{i}_{j}')
         bpji.append(f'bp{i}_{j}')

xi_string=','.join(xi)
yi_string=','.join(yi)
uji_string=','.join(uji)
bji_string=','.join(bji)

lp_code = lp_code + f'int {xi_string},m,M; \n'
lp_code = lp_code + f'int {yi_string}; \n'
lp_code = lp_code + f'bin {uji_string}; \n'
lp_code = lp_code + f'bin {bji_string}; \n'

print(lp_code)

lp_code_lp_file=open(name_of_lp_file, 'w')

lp_code_lp_file.write(lp_code)

lp_code_lp_file.close()
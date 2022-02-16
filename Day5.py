# BMI = weight / height**2

# weight in kilograms
# height in meters

# Four bins:
# Underweight BMI -   < 18.5
# Normal weight   -   18.5 <= BMI < 25.0
# Overweight      -   25.0 <= BMI < 30.0
# Obesity         -   30.0 <= BMI

# input:
# - line 1: #subjects
# - next lines: weight height

# output
# corresponding bin per subject in one line

data = open('Day5_Input.txt', 'r')

bins = []
i = 0
for line in data:
    if i == 0:
        pass #num_entries = int(line)
    else:
        lst = line.split()
        BMI = float(lst[0]) / float(lst[1])**2
        if BMI < 18.5:
            bins.append('under')
        elif BMI >= 18.5 and BMI < 25.0:
            bins.append('normal')
        elif BMI >= 25.0 and BMI < 30.0:
            bins.append('over')
        else:
            bins.append('obese')
    i += 1

answer = ' '.join(bins)

print(answer)
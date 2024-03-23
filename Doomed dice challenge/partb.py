Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]

print(f"Original Dice A = {Die_A}")
print(f"Original Dice B = {Die_B}")

total_combinations = len(Die_A) * len(Die_B)

original_sums = {}
for i in range(len(Die_A)):
    for j in range(len(Die_B)):
        temp = Die_A[i] + Die_B[j]
        val = original_sums.get(temp,0)+1
        original_sums[temp] = val


original_probabilities = {}
for key,val in original_sums.items():
    original_probabilities[key] = val/total_combinations

print("\nOriginal Probabilities: ")
for key,val in original_probabilities.items():
    print(f"P(Sum = {key})  Occurence = {original_sums[key]} \n Probability = {val}")
print("\n")
new_dic = original_sums


diceA = []
diceB = []

def find_diceA_possibility(number,temp):
    if number > 4:
        return
    if len(temp) > 6:
        return
        
    if len(temp) == 6:
        if temp not in diceA:
            diceA.append(temp)
        return
    
        
    for i in range(number,5):
        find_diceA_possibility(i,temp.copy() + [i])
    
def find_diceB_possibility(number,temp):
    if number > 11:
        return
        
    if len(temp) > 6:
        return
        
    if len(temp) == 6:
        if temp not in diceB:
            diceB.append(temp)
        return
        
        
    for i in range(number+1,13):
        find_diceB_possibility(i,temp.copy()+[i])
        
def undoom_dice(Die_A,Die_B):
        
        
    Die_A = Die_B = [0]*6
    print(f"Doomed Dice A = {Die_A}")
    print(f"Doomed Dice B = {Die_B}\n")
    

    for i in range(1,5):
        find_diceA_possibility(i,[i])
    for j in range(1,12):
        find_diceB_possibility(j,[j])
    

    print("Undooming Dice A and Dice B...")
    for i in diceA:
        for j in diceB:
            tdic = {}
            for k in range(len(i)):
                for l in range(len(j)):
                    val = tdic.get(sum([i[k],j[l]]),0)+1
                    tdic[sum([i[k],j[l]])] = val
            
    
            c = 0
            for key,val in tdic.items():
                if val != new_dic.get(key,-1):
                    pass
                else:
                    c+=1
    
            if c == 11:
                return i,j,tdic
New_Die_A,New_Die_B,tdic = undoom_dice(Die_A,Die_B)
print(f"Transformed Dice A -> {New_Die_A}")
print(f"Transformed Dice B -> {New_Die_B}")

print("\nProbability of Dice After Transforming:")
for key,val in tdic.items():
    print(f"P(Sum = {key}) Occurence ={val} \n Probability = {val/total_combinations}")
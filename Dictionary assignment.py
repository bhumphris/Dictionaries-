# Create a dictionary named holidays that pairs the name of
# the holiday with the date it will occur this year, include at least four
# key-value pairs
# example: holiday = {'Independence Day':  'July 4'}

holidays =  dict()
holidays = {'Christmas':'Dec 25', 'Independence Day': 'July 4','Easter': 'Mar 27', 'Presidents day': 'Feb 17' }
print holidays

# print holiday -  does the order match what you put it in?


# run the len function on holiday - how does it calculate the results? ** print(len(holiday))
print(len(holidays))


# Write the code to use the "in" function to find one of the keys in your dictionary. Make sure to surround the
# code with a print statement so that the result prints on screen

print 'Easter' in holidays

# now write the code to look for a key that is not in the dictionary. Make sure to surround the code
# with a print statement so the result prints on screen


print 'Saint Patricks Day' in holidays

# now write the code to find a value in your dictionary, use the print statement to show the results
vals = holidays.values()
key = holidays.keys()

# print all of the values in the dictionary

print vals

# 11.2 Looping and Dictionaries
# Write the histogram code and test it by passing in a word that has at least two of one letter
# Print the result of running the histogram code
def histogram(holidays):
    d = dict()
    for e in holidays:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
        return d
print histogram(holidays)

word = 'Presidents Day'
d = dict()
for e in word:
    if e not in d:
        d[e] = 1
    else:
        d[e] = d[e] + 1
print d



# Exercise 11.2 Rewrite the histogram code using the get method, test with the same word, name the function histogram2
# hint assign the result of d.get(c,0) to a value then add one to the value of d[c]

def histogram2(holidays):
    d = dict()
    for e in holidays:
        d.get(e,0)
        d[e] = 1

print histogram('Presidents Day')



# Looping and Dictionaries
# use a for statement to print your holiday dictionary
# What prints? The keys or the values?
def dictionary_holidays(holidays):
    d = dict()
    for d in holidays:
        print d
hdays = dictionary_holidays(holidays)
    #the keys



print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# now write code that prints all of the keys and all of their values in the holiday dictionary
# if you use the print statement then values separated by commas they appear on the same line
def values(holidays):
    v = dict(vals)
    for d in holidays:
        print d
vdays = vals
print key, vdays

hdays = dictionary_holidays(holidays)
print hdays
print hdays,vdays



vals = str(vals)



print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# Reverse Lookup
# Type the code for the Reverse Lookup from 11.3 below
d = dict(holidays)
v = vals
k = key
def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


# Test the code by calling it with the holiday dictionary and one of your values (print the result)


# Call the code a second time with a value that doesn't exist, run the program


# Copy and paste the error code here, add # as needed to make the error a comment


# leave the line of code that caused the error, but put a # in front of it to make it a comment


# 11.4 Dictionaries and lists
# Type in the code to invert a dictionary
# Call the invert_dict function with the holiday dictionary
# print the results
print ("\n\n")

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
print invert_dict(d)




# Exercise 11.5 Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict. py .



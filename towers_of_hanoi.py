n = 5
start = range(n, 0, -1)
end = []
temp = []

def move_rings(n, start, end, temp):
    if n == 1:
        end.append(start.pop())
        return
    move_rings(n-1, start, end, temp)



    print end

    temp.append(start.pop())
    print end
    end.append(start.pop())
    print end
    end.append(temp.pop())
    #start.append(end.pop())
    #temp.append(end.pop())


print move_rings(n, start, end, temp)

# temp.append(start.pop())
# end.append(start.pop())
#end.append(temp.pop())
#temp.append(start.pop())
#start.append(end.pop())
#temp.append(end.pop())


# s[n] =1
# s[n-1] = 2
# s[n-2] = 3
# s[n-3] = 4

# s[n] --> temp[0]
# s[n-1] --> e[0]
# temp[0] --> e[1]
# s[n-2] --> t[0]
# e[1] --> s[n-2]
# e[0] --> t[1]
# s[n-1] --> t[2]
# s[n-3] --> e[0] BASE CASE
# t[2]--> e[1]
# t[1] --> s[0]
# e[1] --> s[1]
# t[0] --> e[1]
# # s[1] --> t[0]
# # s[0] --> e[2]
# t[0] --> e[3]
email = 'gulnayak@yahoo.com'
atcount = 0
pos_dot = 0
pos_at = 0
dotcount = 0
for i in email:
    if i == '@':
        atcount += 1
if atcount > 1:
    print("invalid")

for i in range(0, len(email)):
    if email[i] == '@':
        pos_at = i

for i in range(pos_at, len(email)):
    if email[i] == '.':
        dotcount += 1

if dotcount > 2 or dotcount < 1:
    print("invalid 2 dots")

for i in range(0, len(email)):
    if email[i] == '@' and email[i + 1] == '.':
        print("invalid dot+at")

c=email[0]
if (c > 'a' and c < 'z') or (c > 'A' and c < 'Z'):
    pass
else:
    print("invalid 1 char b4 @")

for i in range(pos_at,len(email)):
    if email[i]=='.':
        pos_dot=i
        break

email_lst=["gmail","rediffmail","yahoo","hotmail"]
st=email[pos_at+1:pos_dot]
print(st)
if st not in email_lst:
    print("unsupported ")
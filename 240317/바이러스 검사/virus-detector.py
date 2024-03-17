n=int(input())
restaurant = list(map(int,input().split()))
num_manager_scan, num_member_scan = list(map(int,input().split()))


total_scanner = 0 
for client in restaurant:
    # allocate manager
    total_scanner += 1
    rest = client-num_manager_scan
    if rest <= 0:
        continue
    else:
        Q,r = rest//num_member_scan, rest%num_member_scan
        if r == 0:
            total_scanner += Q
        else:
            total_scanner += Q+1
print(total_scanner)
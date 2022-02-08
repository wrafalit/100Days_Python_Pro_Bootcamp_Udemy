auction_off = False
auction_list = []
while not auction_off:
    name = input("What is your name: ")
    bid = int(input("What's your bid?: $"))
    dic = {}
    dic['Name'] = name
    dic['Bid'] = bid
    auction_list.append(dic)
    dic = {}
    other_biders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_biders == 'no':
        auction_off = True
    else:
        print('\n '*30)

# print(auction_list)

for n in range(len(auction_list)):
    dic_winer = {
        "Name" : '',
        "Bid" : 0,
    }
    if auction_list[n]['Bid'] > dic_winer['Bid']:
        dic_winer['Bid'] = auction_list[n]['Bid']
        dic_winer['Name'] = auction_list[n]['Name']

print(f"The winner is {dic_winer['Name']} with a bid of ${dic_winer['Bid']}")



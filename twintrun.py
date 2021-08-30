from twint import get_all_tweets
def main():
    acc_name = input("Enter account name: ")
    res = get_all_tweets(acc_name)#pass acc_name
    print(res[0])
    search = input("Enter search term: ")
    for ele in res:
        if search in ele[-1]:
            print("\nid = ", ele[0], "\nDate and time = ", ele[1], "\nTweet = ", ele[-1],)
        else:
            continue

if __name__ == '__main__':
    main()



def main():
    with open('./ips.txt.txt', 'r') as f:
        for s in f:  
            channels.add(s.strip())
if __name__ == '__main__':
    main()
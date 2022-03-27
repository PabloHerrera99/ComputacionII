import argparse

def main():
    parser = argparse.ArgumentParser(description='copia')
    parser.add_argument("-i", "--input", type = str, required=True, help = "imput file")
    parser.add_argument("-o", "--output", type = str, required=True, help = "destination file")
    args = parser.parse_args()
    
    print('input', args.input)
    print('output', args.output)

    with open(args.input, "r") as inputfile:
        with open(args.output, "w") as outputfile:
            outputfile.write(inputfile.read())
if __name__ == '__main__':
    main()
import sys, getopt
import json

def convert_fields(output_file):
    with open('input.json') as json_file:
        data = json.load(json_file)

        for i, obj in enumerate(data['features'], start=0):
            data['features'][i]['properties']['COUNTYFP'] = int(obj['properties']['COUNTYFP'])

        with open(output_file, 'w') as fp:
            # output to json file and remove whitespace
            json.dump(data, fp, separators=(',', ':'))


def main(argv):
    output_file = 'output.json'
    try:
        opts, _ = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('convert_types.py -o <output_file>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            output_file = arg


    convert_fields(output_file)
    print('Output file is "', output_file)

if __name__ == "__main__":
    main(sys.argv[1:])

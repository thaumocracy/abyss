import pandas

NATO = pandas.read_csv('NATO.csv')
new_NATO = {row[0].lower(): row[1] for (index, row) in NATO.iterrows()}


def clear_word(word):
    try:
        new_word = [new_NATO[item] for item in list(word)]
    except KeyError:
        print('Only alphabet letters,please')
    else:
        return new_word

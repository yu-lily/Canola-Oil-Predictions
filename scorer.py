import csv
import sys
import traceback

def load_labels(filename):
    ret = {}
    with open(filename, newline='', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            region, start_date, end_date = row['Region'], row['Start Date'], row['End Date']
            if row['Deliveries'] != '':
                d = float(row['Deliveries'])
            else:
                d = 0
            if row['Prices'] != '':
                p = float(row['Prices'])
            else:
                p = 0
            ret[(region, start_date, end_date)] = (d, p)
    return ret


def get_score(truth, pred, ids):
    score = 0
    for index in range(2):
        relative_error = 0
        for id in ids:
            assert id in truth
            t = truth[id][index]
            p = pred.get(id, (0, 0))[index]
            relative_error += abs(t - p) / abs(t)
        relative_error = relative_error / len(ids)
        score += max(0, 1 - relative_error)
    score /= 2
    return score * 100


def load_ids(filename, phase):
    assert phase in ['Train', 'Provisional', 'Final']
    ret = []
    for line in open(filename, encoding = 'utf-8'):
        parts = line.strip().split(',')
        if parts[-1] == phase:
            region, start_date, end_date = parts[0], parts[1], parts[2]
            ret.append((region, start_date, end_date))
    return ret


if __name__ == '__main__':
    if len(sys.argv) == 4:
        TRUTHFILE = sys.argv[1]
        PREDFILE = sys.argv[2]
        PHASE = sys.argv[3]
    else:
        TRUTHFILE = 'Hidden_Data/truth.csv'
        PREDFILE = 'example_submission/solution.csv'
        PHASE = 'Provisional'

    truth = load_labels(TRUTHFILE)
    ids = load_ids('Hidden_Data/data_split.csv', PHASE)

    score = 0
    try:
        pred = load_labels(PREDFILE)
        score = get_score(truth, pred, ids)
    except AssertionError as e:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        print('Error Message:', e)
    except FileNotFoundError as e:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        print('Error Message:', e)
    except:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb) # Fixed format
        print('Other Errors!')

    print(f'Final Score = {score}')
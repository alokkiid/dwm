dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes']
]

def separate_by_class(data):
    separated = {}
    for row in data:
        label = row[-1]
        if label not in separated:
            separated[label] = []
        separated[label].append(row)
    return separated

def calculate_prob(attr_index, value, data):
    count = sum(1 for row in data if row[attr_index] == value)
    return count / len(data)

def predict(test):
    separated = separate_by_class(dataset)
    probs = {}
    for label, rows in separated.items():
        probs[label] = 1
        for i in range(len(test)):
            probs[label] *= calculate_prob(i, test[i], rows)
    return max(probs, key=probs.get)

test_case = ['Sunny', 'Cool', 'High', 'Strong']
print("Prediction:", predict(test_case))

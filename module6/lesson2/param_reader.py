def h2i(hexLines):
    if hexLines == '':
        return 0
    return int(hexLines.replace(' ', '').replace(':', ''), 16)


def read_dsa():
    with open('private_parameters', 'r') as f:
        lines = f.readlines()
    f.close()

    params = {}
    currentHex = ''
    currentParam = ''

    for line in lines:
        if line[0].isalpha():
            if currentHex != '' and currentParam != '':
                # print("key:", currentParam)
                params[currentParam] = h2i(currentHex)
            currentParam = line.strip().replace(':', '')[:5]
            currentHex = ''
        else:
            currentHex += line.strip()

    return params
    # print(params)

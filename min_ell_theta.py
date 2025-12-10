# min_ell_theta.py

def learn_theta(data, colors):
    max_blue = None
    max_red = None

    for x, c in zip(data, colors):
        if c == 'blue':
            if max_blue is None or x > max_blue:
                max_blue = x
        if c == 'red':
            if min_red is None or x < min_red:
                min_red = x

    return max_blue + (min_red - max_blue) // 2

def compute_ell(data, colors, theta):
    blue = 0
    red = 0

    for x, c in zip(data, colors):
        if c == 'blue' and x > theta:
            blue += 1
        if c == 'red' and x <= theta:
            red += 1

    return float(blue + red)

def minimize_ell(data, colors):
    n = len(data)
    points = list(zip(data, colors))
    points.sort(key=lambda pair: pair[0])

    thetas = []
    for i in range(n - 1):
        x_i = points[i][0]
        x_next = points[i + 1][0]
        theta = (x_i + x_next) / 2.0
        thetas.append(theta)

    best_theta = None
    best_loss = float("inf")

    for theta in thetas:
        loss = compute_ell(data, colors, theta)
        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return best_theta

    
def minimize_ell_sorted(data, colors):
    n = len(data)

    total_blue = sum(1 for c in colors if c == 'blue')

    red_le_theta = 0
    blue_gt_theta = total_blue

    best_loss = float("inf")
    best_theta = None


    for i in range(n - 1):
        if colors[i] == 'blue':
            blue_gt_theta -= 1
        else:
            red_le_theta += 1

        loss = red_le_theta + blue_gt_theta

        if loss < best_loss:
            best_loss = loss
            best_theta = (data[i] + data[i + 1]) / 2.0

    return best_theta

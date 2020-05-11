def get_num_iter(x, y, z=(0 + 0j), num_iter=0):
    """Determines whether abs(z) diverges and, if so, how many interations it
    takes for abs(z) to diverge

    Parameters:
    x - The x-coordinate (or real part) of point c
    y - The y-coordinate (or imaginary part) of point c
    z - Value that is recursively calculated by z_i+1 = z_i^2 + c (z_0 = 0)
    num_iter - current number of iterations of z (starts at 0)

    Returns:
    Number of iterations at which abs(z) diverges, that is, abs(z) > 10.
    If the number does not diverge, that is, after 50 iterations abs(z) <= 10,
    return 0
    """
    z_new = z**2 + x + y*1j

    if num_iter >= 50:
        return 0

    if abs(z_new) > 10:
        return num_iter

    return get_num_iter(x, y, z_new, num_iter + 1)


def show_plot():
    """Sets reasonable x-axis and y-axis limits, labels the axes, and shows the
    plot

    Parameters:
    Function takes no parameters

    Returns:
    Function has no return value, however, it shows the matplotlib graph
    """
    axis = plt.gca()
    axis.set_xlim([-2, 0.5])
    axis.set_ylim([-1.2, 1.2])
    plt.xlabel("x Axis (Re)")
    plt.ylabel('y Axis (Im)')

    plt.show()


def graph_black_white(xs, ys, colours):
    """Creates graph of points that diverge (drawn in white) and those that do
    not (drawn in black)

    Parameters:
    xs - The list of x-coordinatse (or real part) of the points
    ys - Corresponding list of y-coordinates (or imaginary part) of the points
    colours - Corresponding list of number of iterations before divergence for
    each point (0 if abs(z) does not diverge)

    Returns:
    Function has no return value, however, it shows the matplotlib graph
    """
    for i in range(len(colours)):
        if colours[i] > 0:
            colours[i] = [1, 1, 1]
        else:
            colours[i] = [0, 0, 0]

    plt.scatter(xs, ys, c=colours)
    show_plot()


def graph_coloured(xs, ys, colours):
    """Creates graph of points that diverge (coloured based on number of
    iterations before they converge) and those that do not (drawn in black)

    Parameters:
    xs - The list of x-coordinatse (or real part) of the points
    ys - Corresponding list of y-coordinates (or imaginary part) of the points
    colours - Corresponding list of number of iterations before divergence for
    each point (0 if abs(z) does not diverge)

    Returns:
    Function has no return value, however, it shows the matplotlib graph
    """
    plt.scatter(xs, ys, c=colours, cmap='magma')
    label = r"Number of iterations until $\left| z \right|$ diverges" \
        "\n(0 if it does not diverge)"
    plt.colorbar(label=label)
    show_plot()


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Value controls resolution of the image and calculation time
    incr = 0.01
    xs = []
    ys = []
    num_iters = []

    x = -2
    while x <= 2:
        y = -2
        x = x + incr
        while y <= 2:
            y = y + incr
            xs.append(x)
            ys.append(y)
            num_iters.append(get_num_iter(x, y))

    graph_black_white(xs, ys, num_iters)
    # graph_coloured(xs, ys, num_iters)

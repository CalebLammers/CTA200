def SIR_model(t, y, b, g, N):
    """Calculates the derivative of S, I, and R with respect to time at some t

    Parameters:
    t - The time at which the derivative is to be calculated
    y - Value of S, I, and R at t
    b - Parameter beta in the ODEs
    g - Parameter gamma in the ODEs
    N - Size of the population

    Returns:
    List of derivatives at time t for S, I, and R (in that order)
    """
    s, i, r = y

    return [-b*s*i/N, b*s*i/N - g*i, g*i]


def SIRD_model(t, y, b, g, l, N):
    """Gives the derivative of S, I, R, and D with respect to time at some t

    Parameters:
    t - The time at which the derivative is to be calculated
    y - Value of S, I, R, and D at t
    b - Parameter beta in the ODEs
    g - Parameter gamma in the ODEs
    l - Parameter lambda in the ODEs (see Q3 pdf)
    N - Size of the population

    Returns:
    List of derivatives at time t for S, I, R, and D (in that order)
    """
    s, i, r, d = y

    return [-b*s*i/N, b*s*i/N - g*i - l*i, g*i, l*i]


def plot(values, times, colours, labels):
    """Graphs values vs. times with their respective colours and labels

    Parameters:
    values - List of np arrays which contain the points of the function
    times - np array of corresponding times for all the functions in values
    colours - List of colours in which the functions in values will be graphed
    labels - List of labels for the functions in values

    Returns:
    Function has no return value, however, it shows the matplotlib graph
    """
    for i in range(len(values)):
        plt.plot(times, values[i], colours[i])

    plt.legend(labels)
    plt.xlabel("Time")
    plt.ylabel("Number of People")

    plt.show()


def ODE_solver(y_0, t_0, t_end, dt, params):
    """Uses Scipy's ODE solver to give the function values for S, I, and R or
    S, I, R, and D, depending on whether parameters are passed for the SIR
    model or the modified model that includes deaths

    Parameters:
    y_0 - List consisting of initial values of S, I, and R or S, I, R, and D
    t_0 - Initial time
    t_end - End time
    dt - Increment in time for ODE solver
    params - List consisting of [b, g, N] or [b, g, l, N]

    Returns:
    np array of S, I, and R or S, I, R, and D values for each corresponding
    time in the np array of times, which is also returned
    """
    times = [t_0]
    res = [y_0]

    if len(params) == 3:
        solver = ode(SIR_model).set_integrator('dopri5').set_initial_value(
            y_0, t_0).set_f_params(params[0], params[1], params[2])
    else:
        solver = ode(SIRD_model).set_integrator('dopri5').set_initial_value(
            y_0, t_0).set_f_params(params[0], params[1], params[2], params[3])

    while solver.successful() and solver.t < t_end:
        times.append(solver.t + dt)
        res.append(solver.integrate(solver.t + dt))

    return np.array(res), np.array(times)


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import ode

    # Define all parameters
    y_0 = [999, 1, 0]
    t_0 = 0.0
    b = 0.4
    g = 0.03
    N = 1000
    t_end = 200
    dt = 0.1

    res, times = ODE_solver(y_0, t_0, t_end, dt, [b, g, N])
    s, i, r = res.T

    plot([s, i, r], times, ['b', 'r', 'g'], ['Susceptible', 'Infected',
         'Recovered'])

    ''' SIR model with deaths

    # Define all parameters
    y_0 = [999, 1, 0, 0]
    t_0 = 0.0
    b = 0.2
    g = 0.07
    l = 0.03
    N = 1000
    t_end = 200
    dt = 0.1

    res, times = ODE_solver(y_0, t_0, t_end, dt, [b, g, l, N])
    s, i, r, d = res.T

    plot([s, i, r, d], times, ['b', 'r', 'g', 'k'], ['Susceptible', 'Infected',
         'Recovered', 'Dead'])
    '''

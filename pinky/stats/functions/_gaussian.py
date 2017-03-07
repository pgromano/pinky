import numpy as np

def dist(self, **kwargs):
    minima = kwargs.get('minima', np.array([[0.5, 0.5]]))
    n_peaks = minima.shape[0]
    sigma = kwargs.get('sigma', np.ones((n_peaks, 2))*1e-1)
    theta = kwargs.get('theta', np.zeros(n_peaks))
    amplitude = kwargs.get('amplitude', np.ones(n_peaks))

    x = np.linspace(self.extent[0], self.extent[1], self.bins[0])
    y = np.linspace(self.extent[2], self.extent[3], self.bins[1])
    XX,YY = np.meshgrid(x,y)

    # Change parameter to simpler names
    x0 = list(minima[:,0])
    y0 = list(minima[:,1])
    sx = list(sigma[:,0])
    sy = list(sigma[:,1])
    AA = list(amplitude)

    # Calculate peak structural form
    aa, bb, cc = _shape(sx, sy, theta)

    self.P = 0
    for peak in range(n_peaks):
        self.P += AA[peak]*np.exp(-(aa[peak]*(XX-x0[peak])**2 -
                 2*bb[peak]*(XX-x0[peak])*(YY-y0[peak]) +
                 cc[peak]*(YY-y0[peak])**2))


def _shape(sx, sy, theta):
    aa = np.zeros(len(sx))
    bb = np.copy(aa)
    cc = np.copy(aa)
    for n in range(len(sx)):
        aa[n] =  np.cos(theta[n])**2/(2*sx[n]**2)+np.sin(theta[n])**2/(2*sy[n]**2)
        bb[n] = -np.sin(2*theta[n])/(4*sx[n]**2)+np.sin(2*theta[n])/(4*sy[n]**2)
        cc[n] =  np.sin(theta[n])**2/(2*sx[n]**2)+np.cos(theta[n])**2/(2*sy[n]**2)
    return aa,bb,cc

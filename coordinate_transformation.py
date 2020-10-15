import math
import numpy as np

WGS84_A = 6378137.0
WGS84_f = 1 / 298.257223565
WGS84_E2 = WGS84_f * (2 - WGS84_f)
WGS84_we = 7.2921151467 * 1e-5
WGS84_GM = 3986004.418 * 1e8
c_light = 2.99792458 * 1e8

deg2rad = math.pi / 180.0
rad2deg = 180.0 / math.pi


def xyz2lla(XYZ):
    LLA = [0, 0, 0]
    LLA[0] = np.arctan(XYZ[1] / XYZ[0])

    p = math.sqrt(XYZ[0] ** 2 + XYZ[1] ** 2)

    while True:
        N = WGS84_A / math.sqrt(1 - WGS84_E2 * math.sin(LLA[1]) * math.sin(LLA[1]))
        alt = p / (math.cos(LLA[1]) - N)
        lat = np.arctan((XYZ[2] / p) * (1 - WGS84_E2 * (N / N + alt)))

        if lat - LLA[1] < 0.0000001:
            LLA[1] = lat
            LLA[2] = alt
            break
        else:
            LLA[1] = lat
            LLA[2] = alt
    return LLA


def lla2xyz(LLA):
    XYZ = [0, 0, 0]
    LLA[0] *= deg2rad
    LLA[1] *= deg2rad
    N = WGS84_A / (math.sqrt(1 - WGS84_E2 * math.sin(LLA[1]) * math.sin(LLA[1])))
    XYZ[0] = (N + LLA[2]) * math.cos(LLA[1]) * math.cos(LLA[0])
    XYZ[1] = (N + LLA[2]) * math.cos(LLA[1]) * math.sin(LLA[0])
    XYZ[2] = (N * (1 - WGS84_f) * (1 - WGS84_f) + LLA[2]) * math.sin(LLA[1])
    return XYZ


def xyz2enu(XYZ, XYZ0):
    LLA = xyz2lla(XYZ0)

    sin_p = math.sin(LLA[0])
    cos_p = math.cos(LLA[0])
    sin_l = math.sin(LLA[1])
    cos_l = math.cos(LLA[1])

    S = np.array([[-sin_p, cos_p, 0], [-sin_l * cos_p, -sin_l * sin_p, cos_l], [cos_l * cos_p, cos_l * sin_p, sin_l]])
    delta = np.array([[XYZ[0] - XYZ0[0]], [XYZ[1] - XYZ0[1]], [XYZ[2] - XYZ0[2]]])

    NUE = []
    ENU_2darray = np.dot(S, delta)
    for i in range(3):
        NUE.append(ENU_2darray[i][0])

    ENU=[]
    ENU.append(NUE[2])
    ENU.append(NUE[0])
    ENU.append(NUE[1])

    return ENU


def enu2xyz(ENU, XYZ0):
    LLA = xyz2lla(XYZ0)

    sin_p = math.sin(LLA[0])
    cos_p = math.cos(LLA[0])
    sin_l = math.sin(LLA[1])
    cos_l = math.cos(LLA[1])

    S = np.array([[-sin_p, cos_p, 0], [-sin_l * cos_p, -sin_l * sin_p, cos_l], [cos_l * cos_p, cos_l * sin_p, sin_l]])

    delta_XYZ = np.dot(S.T, ENU)

    XYZ = []
    for i in range(3):
        XYZ.append(XYZ0[i] + delta_XYZ[i])

    return XYZ

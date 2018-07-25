# overall p

x_0   = (412.5, 151.5)
x_300 = (616.5, 151.5)

y_0   = (409.5, 148.5)
y_03  = (409.5, 26.5)


d1    = (424.0, 59.7)
d1_up = (424.0, 50.6)
d1_dw = (424.0, 68.5)

d2    = (447.6, 79.8)
d2_up = (447.6, 74.5)
d2_dw = (447.5, 85.5)

d3    = (471.5, 87.7)
d3_up = (471.5, 82.5)
d3_dw = (471.5, 92.4)

d4    = (495.4, 97.9)
d4_up = (495.6, 92.5)
d4_dw = (495.5, 103.5)

d5    = (519.3, 109.3)
d5_up = (519.5, 102.6)
d5_dw = (519.5, 116.4)

d6    = (543.3, 106.4)
d6_up = (543.5, 96.6)
d6_dw = (543.5, 116.4)

d7    = (567.2, 121.9)
d7_up = (567.5, 110.6)
d7_dw = (567.8, 133.8)

d8    = (590.5, 133.6)
d8_up = (590.5, 121.5)  
d8_dw = (590.4, 144.9)

d9    = (614.5, 119.3)
d9_up = (614.5, 99.5)
d9_dw = (614.5, 139.5)


dps_pix  = [d1, d2, d3, d4, d5, d6, d7, d8, d9]
dps_up_pix = [d1_up, d2_up, d3_up, d4_up, d5_up, d6_up, d7_up, d8_up, d9_up]
dps_dw_pix = [d1_dw, d2_dw, d3_dw, d4_dw, d5_dw, d6_dw, d7_dw, d8_dw, d9_dw]

xvals_data = [(dp[0]-x_0[0])/(x_300[0]-x_0[0])*300 for dp in dps_pix]
yvals_data = [(dp[1]-y_0[1])/(y_03[1]-y_0[1])*0.3 for dp in dps_pix]

yerrs_data = [((dps_up_pix[i][1]-dps_dw_pix[i][1])/2.)/(y_03[1]-y_0[1])*0.3 for i in range(9)]


if __name__ == "__main__":
    print(xvals_data)
    print(yvals_data)
    print(yerrs_data)


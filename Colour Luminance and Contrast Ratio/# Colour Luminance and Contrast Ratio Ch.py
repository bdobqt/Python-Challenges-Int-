# Colour Luminance and Contrast Ratio Challenge 01

print("working!")

# Could add input rules for int 0-255

def luminance (R, G, B) :
    R0 = R / 255
    G0 = G / 255
    B0 = B / 255 
    if (R0 <= 0.03928) :
        R1 = R0 / 12.92
    else:
        temp = (R0 + 0.055) / 1.055
        R1 = pow(temp, 2.4)

    if (G0 <= 0.03928) :
        G1 = G0 / 12.92
    else:
        temp = (G0 + 0.055) / 1.055
        G1 = pow(temp, 2.4)

    if (B0 <= 0.03928) :
        B1 = B0 / 12.92
    else:
        temp = (B0 + 0.055) / 1.055
        B1 = pow(temp, 2.4)
    
    L = (0.2126 * R1) + (0.7152 * G1) + (0.0722 * B1)
    return L


def contrastRatioEval(R, G, B, RR, GG, BB):
    L1 = luminance(R,G,B)
    L2 = luminance(RR,GG,BB)
    if (L1 >= L2 ):
        Llight = L1
        Ldark = L2
    else:
        Ldark = L1
        Llight = L2
    contrastRatio = (Llight + 0.05) / (Ldark + 0.05)
    print("Luminance of light colour : {0:.2%}\nLuminance of dark colour : {1:.2%}\nContrast Ratio : {2}".format(Llight, Ldark, contrastRatio))



#luminance(148,57,173)
#luminance(174,84,199)
contrastRatioEval(148, 57 ,173, 245, 232, 248)
contrastRatioEval(0, 0 ,0, 255, 255, 255)


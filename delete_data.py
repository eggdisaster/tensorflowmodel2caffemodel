with open("conv3d_deepnetA_sport1m_iter_1900000.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    #print(lines)
with open("conv3d_deepnetA_sport1m_iter_1900000_without_data.txt","w",encoding="utf-8") as f_w:
    for line in lines:
        if "data:" in line:
            continue
        f_w.write(line)
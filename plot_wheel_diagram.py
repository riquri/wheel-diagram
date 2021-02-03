import sys
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import matplotlib.patheffects as PathEffects
import subprocess


matplotlib.font_manager._rebuild()


plt.rcParams["font.family"] = "Helvetica"
plt.rcParams["font.weight"] = "bold"

def wheel_diagram(seq):
    result=[]
    RESIDUES = ["A","L","I","V","F","Y","W","M","C","G","P","N","Q","S","T","H","R","K","D","E", "*"]
    kyte_doolittle = [1.8,3.8,4.5,4.2,2.8,-1.3,-0.9,1.9,2.5,-0.4,-1.6,-3.5,-3.5,-0.8,-0.7,-3.2,-4.5,-3.9,-3.5,-3.5, 0]
    cycle = 0
    moment = [0,0]
    for index, res in enumerate(seq):
        result.append([index, cycle, res, kyte_doolittle[RESIDUES.index(res)]])
        moment[0] = moment[0] + (kyte_doolittle[RESIDUES.index(res)] * math.cos(index*100/180*math.pi))
        moment[1] = moment[1] + (kyte_doolittle[RESIDUES.index(res)] * math.sin(index*100/180*math.pi))
        if (index+1)%18 == 0 and index is not 0:
            cycle += 1
    return result, moment, math.sqrt(moment[0]**2+moment[1]**2)/len(seq)


def plot_wheel_diagram(seq):
    initial_radius = 3
    marker_size = 1
    result, moment_vec, moment_val = wheel_diagram(seq)
    prev_point = [initial_radius,0]
    plt.figure(figsize=(4, 4))

    if len(seq) > 18*3:
        font_size = 8
    else:
        font_size = 16

    for res in result:
        if res[2] in ["R", "K", "H"]:
            color="#007AB7"
        elif res[2] in ["D", "E"]:
            color="#C7243A"
        elif res[2] in ["N", "Q", "S", "T"]:
            color="#23AC0E"
        else:
            color="#333333"
        current_point = [math.cos(res[0]*100/180*math.pi)*(initial_radius+res[1]*marker_size),math.sin(res[0]*100/180*math.pi)*(initial_radius+res[1]*marker_size)]
        
        boxdic = {
        "facecolor" : "white",
        "edgecolor" : color,
        "boxstyle" : "Circle",
        "linewidth" : 2
        }

        plt.text(current_point[0], current_point[1], r"$\bf{" + res[2] + "}$", color=color, fontsize=font_size, fontweight="bold", zorder=999-res[0], bbox=None, va="center", ha="center")
        
        c = patches.Circle(xy=(current_point[0]+0.05, current_point[1]-0.05), radius=0.5, linewidth=2, fc="white", ec=color, zorder=999-res[0])
        plt.gca().add_patch(c)
        plt.plot([prev_point[0],current_point[0]],[prev_point[1],current_point[1]], color="#DDDDDD", linewidth=1, zorder=100)
        prev_point = current_point
    final_radius = (initial_radius+result[-1][1]*marker_size)*1.2
    #plt.plot([0,moment_vec[0]/10],[0,moment_vec[1]/10])
    center_text = plt.text(0, 0, "{:.3g}".format(moment_val),ha='center', va="center", zorder=120, fontsize=16, weight="bold", color="#333333")
    center_text.set_path_effects([PathEffects.withStroke(linewidth=3, foreground='w')])
    
    an = plt.annotate("", xy=[moment_vec[0]/30,moment_vec[1]/30], xytext=[0,0], arrowprops=dict(shrink=0, width=2, headwidth=8,headlength=8, connectionstyle='arc3',facecolor="#999999", edgecolor="#999999"))
    an.set_zorder(101)
    plt.xlim(-final_radius, final_radius)
    plt.ylim(-final_radius, final_radius)
    plt.xticks([])
    plt.yticks([])
    plt.gca().invert_yaxis()
    plt.gca().set_aspect("equal")
    plt.margins(0,0)
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(f"{seq[0:8]}_wheel.png", dpi=300,pad_inches = 0)


plot_wheel_diagram(sys.argv[1])


import os,sys

directories = ["0.5pi", "1pi", "1.5pi", "2pi"]

subdirs = ["./exp_logs_phase_seed=1234", "./exp_logs_phase_seed=1235", "./exp_logs_phase_seed=1236"]
scores = []
for subdir in subdirs:
    sub_scores = []
    for directory in directories:
        curr_dir_scores = [directory]
        target_dir = subdir + "/" + directory + "/LA_AASIST_ep100_bs32/t-DCF_EER.txt"
        with open(target_dir, 'r') as f:
            content = f.readlines()
            for line in content:
                if "EER" in line:
                    curr_dir_scores.append(float(line.split("=")[1].strip().split("%")[0]))
                elif "min-tDCF" in line:
                    curr_dir_scores.append(float(line.split("=")[1].strip()))
        sub_scores.append(curr_dir_scores)
    scores.append(sub_scores)

# convert scores to csv
with open("phase_avg_data.csv", 'w') as f:
    for score in scores:
        for line in score:
            f.write(",".join([str(x) for x in line]) + "\n")
            

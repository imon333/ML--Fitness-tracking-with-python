
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

## Load data ---------------------------------------

df = pd.read_pickle("../../data/interim/01_data_processed.pkl")


unique_values = df['set'].unique()
print(unique_values)

## plot single columns ------------------------------

set_df = df[df["set"] == 2]
plt.plot(set_df["acc_y"])

plt.plot(set_df["acc_y"].reset_index(drop=True))


#plot all exercise ----------------------------------

for label in df["label"].unique():
    subset = df[df["label"] == label]
    fig, ax = plt.subplots()
    plt.plot(subset["acc_y"].reset_index(drop=True),label = label)
    plt.legend()
    plt.show()
    
for label in df["label"].unique():
    subset = df[df["label"] == label]
    fig, ax = plt.subplots()
    plt.plot(subset[:100]["acc_y"].reset_index(drop=True),label = label)
    plt.legend()
    plt.show()
    
## Adjust plot setting --------------------------------

mpl.style.use("seaborn-v0_8-deep")
mpl.rcParams["figure.figsize"] = (20,5)
mpl.rcParams["figure.dpi"] = 100

## Compare medium vs. heavy sets --------------------------------

category_df = df.query("label =='squat' ").query("participant == 'A'").reset_index()

fig, ax = plt.subplots()
category_df.groupby(["category"])["acc_y"].plot()
ax.set_ylabel("Acc_y")
ax.set_xlabel("Samples")
plt.legend()

## Compare Participants --------------------------------

participant_df = df.query("label =='bench' ").sort_values("participant").reset_index()

fig, ax = plt.subplots()
participant_df.groupby(["participant"])["acc_y"].plot()
ax.set_ylabel("Acc_y")
ax.set_xlabel("Samples")
plt.legend()


## plot multiple axis -------------------------------------
label = "squat"
participant = "A"
all_axis_df = df.query(f"label == '{label}' ").query(f"participant == '{participant}' ")


fig, ax = plt.subplots()
all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
ax.set_ylabel("Acc_y")
ax.set_xlabel("Samples")
plt.legend()

## create a loop to plot all combinations per sensor

labels = df["label"].unique()
participants = df["participant"].unique()

for label in labels:
    for participant in participants:
        all_axis_df =(
            df.query(f"label == '{label}' ")
            .query(f"participant == '{participant}' ")
            .reset_index()
        )
        
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["acc_x","acc_y","acc_z"]].plot(ax = ax)
            ax.set_ylabel("Acc_y")
            ax.set_xlabel("Samples")
            plt.title(f"{label}({participant})".title())
            plt.legend()

## for gyr_--------------------------------

for label in labels:
    for participant in participants:
        all_axis_df =(
            df.query(f"label == '{label}' ")
            .query(f"participant == '{participant}' ")
            .reset_index()
        )
        
        if len(all_axis_df) > 0:
            fig, ax = plt.subplots()
            all_axis_df[["gyr_x","gyr_y","gyr_z"]].plot(ax = ax)
            ax.set_ylabel("gyr_y")
            ax.set_xlabel("Samples")
            plt.title(f"{label}({participant})".title())
            plt.legend()

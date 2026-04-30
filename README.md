# Team-Selector

# 🏏 Cricket Team Selector — IPL Auction Simulator

## 📌 Overview

The **Cricket Team Selector** is a Python-based project that simulates an IPL-style auction system. It selects the **best possible Playing XI (11 players)** within a given budget while maximizing the overall team rating.

The project combines:

* **Dynamic Programming (0/1 Knapsack Algorithm)** for optimal team selection
* **Greedy Strategy** for intelligent player suggestions

---

## 🎯 Objectives

* Select **11 players** within a fixed budget
* Maximize **total team rating**
* Maintain **balanced team composition**
* Provide **smart suggestions** for better decisions

---

## 🧠 Algorithms Used

### 🔹 1. Dynamic Programming (0/1 Knapsack)

* Players are treated as items
* Cost = weight
* Rating = value
* Budget = capacity

**Goal:**
Maximize total rating without exceeding budget.

---

### 🔹 2. Greedy Algorithm

* Used for suggesting best remaining players

* Based on:

  `Efficiency = Rating / Cost`

* Helps users make quick decisions

---

## 🗂️ Features

✔ IPL-style auction simulation
✔ Budget-based team selection
✔ Role-based constraints (Batsman, Bowler, etc.)
✔ Optimal player selection using DP
✔ Greedy-based suggestions
✔ Colored terminal UI
✔ Player statistics display
✔ Team balance validation

---

## 🧩 Team Composition Rules

* Minimum 3 Batsmen
* Minimum 1 Wicket Keeper
* Minimum 2 All-Rounders
* Minimum 4 Bowlers
* Total players = 11

---

## ⚙️ How It Works

1. Display available player pool
2. User enters auction budget
3. System selects mandatory players by role
4. Apply **Knapsack DP** for optimal selection
5. Validate team balance
6. Show:

   * Selected players
   * Remaining budget
   * Team stats
7. Provide **Greedy suggestion**

---

## 📊 Complexity

* **Time Complexity:** `O(n × W)`
* **Space Complexity:** `O(n × W)`

Where:

* `n` = number of players
* `W` = budget

---

## 🖥️ How to Run

### 🔹 Requirements

* Python 3.x

### 🔹 Steps

```bash
# Clone the repository
git clone https://github.com/your-username/cricket-team-selector.git

# Navigate to project folder
cd cricket-team-selector

# Run the program
python main.py
```

---

## 📷 Sample Output

* Displays:

  * Player pool
  * Selected Playing XI
  * Budget usage bar
  * Team composition
  * Suggestions

---

## 💡 Key Highlights

* Hybrid approach: **DP + Greedy**
* Real-world inspired (IPL auction system)
* Ensures optimal and balanced team
* Interactive CLI experience

---

## 🚀 Future Enhancements

* GUI version (using Tkinter/React)
* Real player stats API integration
* Multiple team comparison
* Tournament simulation

---

## 👨‍💻 Author

**Vamsi Krishna**

---

## 📄 License

This project is open-source and available under the MIT License.

# ================================================================
#  🏏 CRICKET TEAM SELECTOR
#  Algorithm: 0/1 Knapsack (Dynamic Programming) + Greedy
#  Like IPL Auction — Select Best 11 Players Within Budget
# ================================================================



# ── TERMINAL COLORS ─────────────────────────────────────────────
class C:
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    RED    = '\033[91m'
    CYAN   = '\033[96m'
    PURPLE = '\033[95m'
    BLUE   = '\033[94m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'
    DIM    = '\033[2m'
    WHITE  = '\033[97m'

def green(t):  return f"{C.GREEN}{t}{C.RESET}"
def yellow(t): return f"{C.YELLOW}{t}{C.RESET}"
def red(t):    return f"{C.RED}{t}{C.RESET}"
def cyan(t):   return f"{C.CYAN}{t}{C.RESET}"
def purple(t): return f"{C.PURPLE}{t}{C.RESET}"
def blue(t):   return f"{C.BLUE}{t}{C.RESET}"
def bold(t):   return f"{C.BOLD}{t}{C.RESET}"
def dim(t):    return f"{C.DIM}{t}{C.RESET}"


# ── PLAYER DATABASE ─────────────────────────────────────────────
# Each player: name, cost (crores), rating (1-100), role, country
def get_player_pool():
    return [
        # Batsmen
        {"name": "Virat Kohli",      "cost": 15, "rating": 95, "role": "Batsman",    "country": "India",       "bat": 95, "bowl": 10, "field": 90},
        {"name": "Rohit Sharma",     "cost": 14, "rating": 92, "role": "Batsman",    "country": "India",       "bat": 92, "bowl": 15, "field": 85},
        {"name": "David Warner",     "cost": 12, "rating": 88, "role": "Batsman",    "country": "Australia",   "bat": 88, "bowl": 5,  "field": 82},
        {"name": "Kane Williamson",  "cost": 11, "rating": 87, "role": "Batsman",    "country": "New Zealand", "bat": 87, "bowl": 20, "field": 80},
        {"name": "Babar Azam",       "cost": 13, "rating": 90, "role": "Batsman",    "country": "Pakistan",    "bat": 90, "bowl": 5,  "field": 83},
        {"name": "Steve Smith",      "cost": 10, "rating": 85, "role": "Batsman",    "country": "Australia",   "bat": 85, "bowl": 18, "field": 78},
        {"name": "Shubman Gill",     "cost": 8,  "rating": 80, "role": "Batsman",    "country": "India",       "bat": 80, "bowl": 5,  "field": 85},
        {"name": "KL Rahul",         "cost": 11, "rating": 83, "role": "WK-Batsman", "country": "India",       "bat": 83, "bowl": 0,  "field": 88},

        # All-Rounders
        {"name": "Ben Stokes",       "cost": 14, "rating": 93, "role": "All-Rounder","country": "England",     "bat": 85, "bowl": 80, "field": 90},
        {"name": "Hardik Pandya",    "cost": 13, "rating": 88, "role": "All-Rounder","country": "India",       "bat": 80, "bowl": 75, "field": 85},
        {"name": "Shakib Al Hasan",  "cost": 9,  "rating": 84, "role": "All-Rounder","country": "Bangladesh",  "bat": 75, "bowl": 82, "field": 78},
        {"name": "Ravindra Jadeja",  "cost": 12, "rating": 89, "role": "All-Rounder","country": "India",       "bat": 72, "bowl": 85, "field": 95},
        {"name": "Marcus Stoinis",   "cost": 7,  "rating": 76, "role": "All-Rounder","country": "Australia",   "bat": 74, "bowl": 70, "field": 80},
        {"name": "Mitchell Marsh",   "cost": 8,  "rating": 78, "role": "All-Rounder","country": "Australia",   "bat": 76, "bowl": 72, "field": 78},

        # Wicket Keepers
        {"name": "MS Dhoni",         "cost": 12, "rating": 91, "role": "Wicket Keeper","country": "India",     "bat": 80, "bowl": 0,  "field": 98},
        {"name": "Jos Buttler",      "cost": 13, "rating": 90, "role": "Wicket Keeper","country": "England",   "bat": 88, "bowl": 0,  "field": 90},
        {"name": "Rishabh Pant",     "cost": 11, "rating": 85, "role": "Wicket Keeper","country": "India",     "bat": 83, "bowl": 0,  "field": 87},
        {"name": "Quinton de Kock",  "cost": 9,  "rating": 82, "role": "Wicket Keeper","country": "S. Africa", "bat": 80, "bowl": 0,  "field": 85},

        # Bowlers
        {"name": "Jasprit Bumrah",   "cost": 14, "rating": 95, "role": "Bowler",     "country": "India",       "bat": 10, "bowl": 95, "field": 80},
        {"name": "Pat Cummins",      "cost": 13, "rating": 92, "role": "Bowler",     "country": "Australia",   "bat": 25, "bowl": 92, "field": 82},
        {"name": "Mitchell Starc",   "cost": 11, "rating": 88, "role": "Bowler",     "country": "Australia",   "bat": 20, "bowl": 88, "field": 78},
        {"name": "Kagiso Rabada",    "cost": 10, "rating": 87, "role": "Bowler",     "country": "S. Africa",   "bat": 18, "bowl": 87, "field": 75},
        {"name": "Shaheen Afridi",   "cost": 9,  "rating": 85, "role": "Bowler",     "country": "Pakistan",    "bat": 12, "bowl": 85, "field": 72},
        {"name": "Trent Boult",      "cost": 8,  "rating": 83, "role": "Bowler",     "country": "New Zealand", "bat": 15, "bowl": 83, "field": 74},
        {"name": "Ravichandran Ashwin","cost":10, "rating": 86, "role": "Bowler",     "country": "India",       "bat": 35, "bowl": 86, "field": 70},
        {"name": "Adil Rashid",      "cost": 6,  "rating": 75, "role": "Bowler",     "country": "England",     "bat": 20, "bowl": 75, "field": 70},
        {"name": "Yuzvendra Chahal", "cost": 7,  "rating": 78, "role": "Bowler",     "country": "India",       "bat": 8,  "bowl": 78, "field": 72},
        {"name": "Wanindu Hasaranga","cost": 8,  "rating": 80, "role": "Bowler",     "country": "Sri Lanka",   "bat": 30, "bowl": 80, "field": 75},
    ]


# ── ROLE EMOJI ───────────────────────────────────────────────────
def role_icon(role):
    icons = {
        "Batsman":       "🏏",
        "WK-Batsman":    "🧤",
        "All-Rounder":   "⚡",
        "Wicket Keeper": "🧤",
        "Bowler":        "🎯",
    }
    return icons.get(role, "🏏")


# ── RATING COLOR ─────────────────────────────────────────────────
def rating_color(r):
    if r >= 90: return green(f"{r}")
    if r >= 80: return yellow(f"{r}")
    return red(f"{r}")


# ================================================================
#  🧠 0/1 KNAPSACK — DYNAMIC PROGRAMMING
#  Select best players within budget, max 11 players
#  Weight = cost (crores), Value = rating
# ================================================================
def knapsack(players, budget, max_players=11):
    # Step 1: Mandatory role picks
    mandatory = []
    mandatory_roles = {"Batsman": 3, "Wicket Keeper": 1, "All-Rounder": 2, "Bowler": 4}
    remaining_budget = budget

    for role, count in mandatory_roles.items():
        pool = sorted(
            [p for p in players if p["role"] in (
                ["Batsman", "WK-Batsman"] if role == "Batsman" else
                ["Wicket Keeper"]           if role == "Wicket Keeper" else
                ["All-Rounder"]             if role == "All-Rounder" else
                ["Bowler"]
            ) and p["cost"] <= remaining_budget],
            key=lambda x: x["rating"], reverse=True
        )
        picked = 0
        for p in pool:
            if picked >= count: break
            if p not in mandatory and p["cost"] <= remaining_budget:
                mandatory.append(p)
                remaining_budget -= p["cost"]
                picked += 1

    # Step 2: DP on remaining players to fill up to 11
    remaining_players = [p for p in players if p not in mandatory]
    slots_left = max_players - len(mandatory)
    n = len(remaining_players)
    W = remaining_budget

    dp    = [[(0, 0)] * (W + 1) for _ in range(n + 1)]
    chose = [[False]  * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost   = remaining_players[i - 1]["cost"]
        rating = remaining_players[i - 1]["rating"]
        for w in range(W + 1):
            prev_rating, prev_count = dp[i - 1][w]
            dp[i][w] = dp[i - 1][w]
            chose[i][w] = False
            if cost <= w:
                new_rating = dp[i - 1][w - cost][0] + rating
                new_count  = dp[i - 1][w - cost][1] + 1
                if new_count <= slots_left and new_rating > prev_rating:
                    dp[i][w]   = (new_rating, new_count)
                    chose[i][w] = True

    extra = []
    w = W
    for i in range(n, 0, -1):
        if chose[i][w]:
            extra.append(remaining_players[i - 1])
            w -= remaining_players[i - 1]["cost"]

    selected     = mandatory + extra
    not_selected = [p for p in players if p not in selected]
    total_rating = sum(p["rating"] for p in selected)
    return total_rating, selected, not_selected


# ================================================================
#  GREEDY SUGGESTION
#  Best unselected player by rating/cost ratio
# ================================================================
def greedy_suggestion(not_selected, remaining_budget):
    if not not_selected:
        return "Perfect squad selected!"

    ranked = sorted(
        not_selected,
        key=lambda p: p['rating'] / p['cost'],
        reverse=True
    )
    top   = ranked[0]
    ratio = top['rating'] / top['cost']
    short = top['cost'] - remaining_budget

    tip = f"Best available: {top['name']} ({top['role']}) — Rating/Cost ratio: {ratio:.1f}. "
    if short > 0:
        tip += f"Need ₹{short}Cr more to afford them."
    else:
        tip += f"You can still afford them with ₹{remaining_budget}Cr remaining!"
    return tip


# ================================================================
#  TEAM BALANCE CHECKER
#  Check if team has minimum required roles
# ================================================================
def check_team_balance(selected):
    roles = {
        "batsmen":    0,
        "allrounders":0,
        "keepers":    0,
        "bowlers":    0,
    }
    for p in selected:
        r = p['role']
        if r in ["Batsman", "WK-Batsman"]:
            roles["batsmen"] += 1
        elif r == "All-Rounder":
            roles["allrounders"] += 1
        elif r == "Wicket Keeper":
            roles["keepers"] += 1
        elif r == "Bowler":
            roles["bowlers"] += 1

    issues = []
    if roles["batsmen"] < 3:
        issues.append(f"Need at least 3 batsmen (have {roles['batsmen']})")
    if roles["keepers"] < 1:
        issues.append(f"Need at least 1 wicket keeper (have {roles['keepers']})")
    if roles["bowlers"] < 4:
        issues.append(f"Need at least 4 bowlers (have {roles['bowlers']})")

    return roles, issues


# ================================================================
#  PRINT FUNCTIONS
# ================================================================
def print_header():
    print()
    print(bold(cyan("=" * 65)))
    print(bold(cyan("   🏏  CRICKET TEAM SELECTOR  🏆")))
    print(bold(cyan("   IPL-Style Auction — DP Knapsack Algorithm")))
    print(bold(cyan("=" * 65)))
    print()

def print_section(title):
    print()
    print(bold(f"── {title} " + "─" * (55 - len(title))))

def print_player_table(players, title, show_index=True):
    print_section(title)
    if not players:
        print(dim("  No players."))
        return

    print(f"  {'#':<4} {'Name':<22} {'Role':<16} {'Country':<14} {'Cost':>6} {'Rating':>8} {'Bat':>5} {'Bowl':>5}")
    print(dim("  " + "─" * 85))

    for i, p in enumerate(players, 1):
        idx = f"{i}" if show_index else "•"
        print(
            f"  {idx:<4} {p['name']:<22} "
            f"{role_icon(p['role'])} {p['role']:<14} "
            f"{p['country']:<14} "
            f"{yellow(f'₹{p[chr(99)+chr(111)+chr(115)+chr(116)]}Cr'):>14} "
            f"{rating_color(p['rating']):>16} "
            f"{dim(str(p['bat'])):>13} "
            f"{dim(str(p['bowl'])):>13}"
        )

def print_progress_bar(value, total, width=40):
    pct    = min(value / total, 1.0)
    filled = int(pct * width)
    bar    = green("█" * filled) + dim("░" * (width - filled))
    return f"[{bar}] {pct*100:.1f}%"


# ================================================================
#  MAIN PROGRAM
# ================================================================
def main():
    print_header()

    players = get_player_pool()

    # ── STEP 1: Show available players ──────────────────────────
    print_section("AVAILABLE PLAYER POOL")
    print(f"  Total Players Available : {cyan(str(len(players)))}")
    print(f"  {'Name':<22} {'Role':<16} {'Country':<14} {'Cost':>8} {'Rating':>8}")
    print(dim("  " + "─" * 75))
    for p in players:
        print(
            f"  {p['name']:<22} "
            f"{role_icon(p['role'])} {p['role']:<14} "
            f"{p['country']:<14} "
            f"{yellow(f'₹{p[chr(99)+chr(111)+chr(115)+chr(116)]}Cr'):>14} "
            f"{rating_color(p['rating']):>16}"
        )

    # ── STEP 2: Budget Input ─────────────────────────────────────
    print_section("AUCTION BUDGET SETUP")
    print(dim("  Like IPL — Set your total budget to buy 11 players"))
    print()

    while True:
        try:
            budget = int(input(bold("  Enter total auction budget (₹ Crores, e.g. 90): ₹")))
            if budget > 0:
                break
            print(red("  Budget must be greater than 0"))
        except ValueError:
            print(red("  Enter a valid number"))

    total_player_cost = sum(p['cost'] for p in players)
    print()
    print(f"  Your Budget        : {green(f'₹{budget} Crores')}")
    print(f"  Total Pool Value   : {yellow(f'₹{total_player_cost} Crores')}")
    print(f"  Max Players        : {cyan('11')}")

    # ── STEP 3: Run DP ───────────────────────────────────────────
    input(bold(f"\n  Press Enter to run DP Team Selection..."))

    max_rating, selected, not_selected = knapsack(players, budget, max_players=11)

    # ── STEP 4: Results ──────────────────────────────────────────
    total_spent    = sum(p['cost'] for p in selected)
    remaining      = budget - total_spent
    avg_rating     = sum(p['rating'] for p in selected) / len(selected) if selected else 0
    roles, issues  = check_team_balance(selected)

    print()
    print(bold(cyan("=" * 65)))
    print(bold(cyan("   ✅  YOUR SELECTED TEAM")))
    print(bold(cyan("=" * 65)))

    # Stats
    print()
    print(f"  {bold('Players Selected')}  : {green(str(len(selected)))} / 11")
    print(f"  {bold('Total Spent')}       : {yellow(f'₹{total_spent} Crores')}")
    print(f"  {bold('Remaining Budget')}  : {cyan(f'₹{remaining} Crores')}")
    print(f"  {bold('Total Rating')}      : {purple(str(max_rating))}")
    print(f"  {bold('Average Rating')}    : {green(f'{avg_rating:.1f}')}")
    print()
    print(f"  Budget Used : {print_progress_bar(total_spent, budget)}")

    # Team Composition
    print()
    print(f"  {bold('Team Composition:')}")
    print(f"  Batsmen      : {cyan(str(roles['batsmen']))}")
    print(f"  All-Rounders : {cyan(str(roles['allrounders']))}")
    print(f"  Wkt Keepers  : {cyan(str(roles['keepers']))}")
    print(f"  Bowlers      : {cyan(str(roles['bowlers']))}")

    # Balance warnings
    if issues:
        print()
        for issue in issues:
            print(f"  {yellow('⚠ WARNING:')} {issue}")
    else:
        print()
        print(f"  {green('✓ Balanced Team — All role requirements met!')}")

    # Selected players table
    print_section("✅ SELECTED PLAYERS (PLAYING XI)")
    print(f"  {'#':<4} {'Name':<22} {'Role':<16} {'Country':<14} {'Cost':>8} {'Rating':>8}")
    print(dim("  " + "─" * 75))

    for i, p in enumerate(selected, 1):
        print(
            f"  {green(str(i)):<12} {p['name']:<22} "
            f"{role_icon(p['role'])} {p['role']:<14} "
            f"{p['country']:<14} "
            f"{yellow(f'₹{p[chr(99)+chr(111)+chr(115)+chr(116)]}Cr'):>14} "
            f"{rating_color(p['rating']):>16}"
        )

    # Not selected
    if not_selected:
        print_section("❌ NOT SELECTED (BUDGET EXCEEDED / LIMIT REACHED)")
        print(f"  {'Name':<22} {'Role':<16} {'Cost':>8} {'Rating':>8} {'Reason'}")
        print(dim("  " + "─" * 70))
        for p in not_selected[:8]:
            reason = "Budget" if p['cost'] > remaining else "11-player limit"
            print(
                f"  {red('✗'):<9} {p['name']:<22} "
                f"{p['role']:<16} "
                f"{yellow(f'₹{p[chr(99)+chr(111)+chr(115)+chr(116)]}Cr'):>14} "
                f"{rating_color(p['rating']):>16}  "
                f"{dim(reason)}"
            )

    # Greedy tip
    print_section("💡 GREEDY SUGGESTION")
    print(f"  {yellow(greedy_suggestion(not_selected, remaining))}")

    # Algorithm info
    print_section("📊 ALGORITHM INFO")
    print(f"  Algorithm       : {cyan('0/1 Knapsack — Dynamic Programming')}")
    print(f"  Time Complexity : {dim(f'O(n × W) = O({len(players)} × {budget})')}")
    print(f"  Space Complexity: {dim(f'O(n × W) = O({len(players)} × {budget})')}")
    print(f"  Players Pool    : {dim(str(len(players)))}")
    print(f"  Budget (W)      : {dim(f'₹{budget} Crores')}")

    print()
    print(bold(cyan("=" * 65)))
    print(bold(cyan("   🏆  Team Selected! Push to GitHub & Submit 🚀")))
    print(bold(cyan("=" * 65)))
    print()


# ── Entry Point ──────────────────────────────────────────────────
if __name__ == '__main__':
    main()
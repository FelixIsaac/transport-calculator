def cal_budget(current, goal, months):
    if current > goal:
        return goal("You have already met your budget goal")

    reminding = goal - current
    print("You have to save ${:.2f} per month to reach your desired budget goal.".format(reminding / months))
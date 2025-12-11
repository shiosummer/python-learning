def powerup(power,times):
    if times<365:
        power=power+power*0.01
        return powerup(power,times+1)
    else:
        return power
def powerdown(power,times):
    if times<365:
        power=power-power*0.01
        return powerdown(power,times+1)
    else:
        return power

print(powerup(1,0))
print(powerdown(1,0))
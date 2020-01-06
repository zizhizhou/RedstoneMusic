import tools, time
# 输入TNT数量，0表示无限
def tntfollow(number):
    mc=tools.start(0)
    spawn=mc.spawnEntity
    pId=mc.getPlayerEntityId(map(mc.entity.getName, mc.getPlayerEntityIds()))
    start=mc.entity.getTilePos(pId)
    if number==0:
        while True:
            spawn(pos.up(7), entity.PRIMED_TNT.id)
            pos = mc.entity.getTilePos(pId)
            time.sleep(1)
    else:
        i = 0
        while i < number:
            spawn(pos.up(7), entity.PRIMED_TNT.id)
            pos = mc.entity.getTilePos(pId)
            time.sleep(1)
            i += 1

from collections import deque

class dispenser:
    def __init__(self,code,fuel):
        self.code=code
        self.remaining_fuel=fuel
        self.busy_time=0
    def fuel(self,liters):
        if self.remaining_fuel < liters:
            raise Exception("in sufficient fuel")
        self.remaining_fuel-=liters
        self.busy_time=liters

def solution(a,x,y,z):
    if max(a) > max([x,y,z]):
        return -1
    if sum(a) > sum([x,y,z]):
        return -1
    #build fuel dispenser dic
    disp_dic=dict({'x':dispenser('x',x),'y':dispenser('y',y),'z':dispenser('z',z)})
    #build car queue
    waiting_t=-1
    next_disp=sufficient_disp=None
    car_queue=deque(a)
    while car_queue:
        c=car_queue[0] #peek
        for d in [i for i in disp_dic if len(car_queue)>0]:
            if c<=disp_dic[d].remaining_fuel and disp_dic[d].busy_time==0:
                fuel = car_queue.popleft() #dequeue
                disp_dic[d].fuel(fuel)
                break
        else:
            #select sufficient fuel dispenser with less waiting time, otherwise no cars then exit
            sufficient_disp=[i for i in disp_dic if c <= disp_dic[i].remaining_fuel]
            if len(sufficient_disp)==0:
                return -1
            next_disp=min(sufficient_disp,key=lambda i:disp_dic[i].busy_time)
            waiting_t=max(disp_dic[next_disp].busy_time,waiting_t)
            disp_dic[next_disp].busy_time=0
    return waiting_t

print(solution([2,8,4,3,2],7,11,3))

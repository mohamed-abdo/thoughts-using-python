from collections import deque


class dispenser:
    def __init__(self, code, fuel):
        self.code = code
        self.remaining_fuel = fuel
        self.busy_time = 0

    def fuel(self, liters):
        if self.remaining_fuel < liters:
            raise Exception("insufficient fuel")
        self.remaining_fuel -= liters
        self.busy_time = liters


def calc_max_waiting_time(cars_list, *dispensers):
    if max(cars_list) > max(*dispensers):
        return -1
    if sum(cars_list) > sum([*dispensers]):
        return -1
    # build fuel dispenser dic
    disp_dic = {'dispenser_{}'.format(i): dispenser('dispenser_{}'.format(i), v)
                for i, v in enumerate(dispensers)}
    # build car queue
    waiting_t = 0
    next_disp = sufficient_disp = None
    car_queue = deque(cars_list)
    while car_queue:
        c = car_queue[0]  # peekß
        for d in [i for i in disp_dic if len(car_queue) > 0]:
            if c <= disp_dic[d].remaining_fuel and disp_dic[d].busy_time == 0:
                fuel = car_queue.popleft()  # dequeue
                disp_dic[d].fuel(fuel)
                break
        else:
            # select sufficient fuel dispenser with less waiting time, otherwise no cars then exit
            sufficient_disp = [i for i in disp_dic if c <=
                               disp_dic[i].remaining_fuel]
            if len(sufficient_disp) == 0:
                return -1
            next_disp = min(sufficient_disp,
                            key=lambda i: disp_dic[i].busy_time)
            waiting_t = max(disp_dic[next_disp].busy_time, waiting_t)
            disp_dic[next_disp].busy_time = 0
    return waiting_t


# basic unit test
def test_calc_max_waiting_time_with_wait():
    assert 8 == calc_max_waiting_time([2, 8, 4, 3, 2], 7, 11, 3), 'invalid result'


def test_calc_max_waiting_time_with_no_wait():
    assert 0 == calc_max_waiting_time([2, 8, 4, 3, 12], 2, 8, 4, 3, 12), 'invalid result'


def test_calc_max_waiting_time_max_liters():
    assert -1 == calc_max_waiting_time([20, 8, 4, 3, 2], 7, 11, 3), 'invalid result'


def test_calc_max_waiting_time_sum_cars_liters():
    assert -1 == calc_max_waiting_time([2, 8, 4, 3, 12], 8, 11, 3), 'invalid result'


# print one result
print('calc_max_waiting_time: ',
      calc_max_waiting_time([2, 8, 4, 3, 2], 7, 11, 3))

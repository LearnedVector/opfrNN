a = [3, 7, 2, 3, 1, 2, 5, 3, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2, 3, 0, 1]
b = [3, 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
c = [4, 1, 2, 3, 4, 5, 0, 6, 2, 0, 3, 1, 6]


# Optimal Page Replacement Algorithm
def optimal_page_replacement(a, m=3):
    n = len(a)
    x = 0
    page_faults = 0
    page = []
    FREE = -1
    for i in range(m):
        page.append(FREE)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            # look for an empty one
            faulted = False
            new_slot = FREE
            for q in range(m):
                if page[q] == FREE:
                    faulted = True
                    new_slot = q

            if not faulted:
                # find next use farthest in future
                max_future = 0
                max_future_q = FREE
                for q in range(m):
                    if page[q] != FREE:
                        found = False
                        for ii in range(i, n):
                            if a[ii] == page[q]:
                                found = True
                                if ii > max_future:
                                    # print "\n\tFound what will be used last: a[%d] = %d" % (ii, a[ii]),
                                    max_future = ii
                                    max_future_q = q

                                break

                        if not found:
                            # print "\n\t%d isn't used again." % (page[q]),
                            max_future_q = q
                            break

                faulted = True
                new_slot = max_future_q

            page_faults += 1
            page[new_slot] = a[i]
    return page_faults

optimal_page_replacement(c)

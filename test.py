import copy as copy


# function returns a list of vectors containing the first input x's neighborhood.
def generate_neighborhood(x=[], neighborhood=[], current_span=[], delta=1):
    if len(x) == 1:
        span1 = list(current_span)
        span1.append(x[0]-delta)
        span2 = list(current_span)
        span2.append(x[0])
        span3 = list(current_span)
        span3.append(x[0]+delta)
        neighborhood.append(span1)
        neighborhood.append(span2)
        neighborhood.append(span3)
        return neighborhood
    else:
        new_span = list(current_span)
        new_span.append(x[0])
        neighborhood = generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
        new_span[-1] = new_span[-1] - delta
        neighborhood = generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
        new_span[-1] = new_span[-1] + 2*delta
        neighborhood = generate_neighborhood(x=x[1:], neighborhood=neighborhood, current_span=new_span)
    return neighborhood


res = generate_neighborhood(x=[5])
print(res)
print(len(res))
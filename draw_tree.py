import turtle


def tree(branchlen, t, size):
    if branchlen > 5:
        t.forward(branchlen)
        t.right(20)
        t.pensize(size)
        tree(branchlen - 15, t, size-1)
        t.left(40)
        t.pensize(size)
        tree(branchlen - 15, t, size-1)
        t.right(20)
        t.backward(branchlen)


if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.pencolor('brown')
    size = 6
    t.pensize(size)
    tree(90, t, size)
    myWin.exitonclick()

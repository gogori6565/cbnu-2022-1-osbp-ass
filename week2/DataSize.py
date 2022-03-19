import sys

#변수 선언
a, b, c, d, e, f, g, h=[None]*8

# 메인 코드
if __name__ == '__main__' :

    a=0
    b=0.0
    c=True
    d=''
    e=[]
    f=()
    g={}
    h=set()
    
    print('int형 기본 크기 --> ',sys.getsizeof(a))
    print('float형 기본 크기 --> ',sys.getsizeof(b))
    print('bool형 기본 크기 --> ',sys.getsizeof(c))
    print('str형 기본 크기 --> ',sys.getsizeof(d))
    print('list형 기본 크기 --> ',sys.getsizeof(e))
    print('tuple형 기본 크기 --> ',sys.getsizeof(f))
    print('dictionary형 기본 크기 --> ',sys.getsizeof(g))
    print('set형 기본 크기 --> ',sys.getsizeof(h))

# 2021041075 이주현

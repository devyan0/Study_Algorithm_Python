
"""
파이썬을 차별화하는 독특한 기능이며, 파이써닉한 테크닉이므로 사용하면 좋다
사후 조건과 사전 조건을 실행할 때 유용하다
일반적으로 리소스 관리를 위해 사용되며
공식 홈페이지에 다양한 사용 예시가 나와있다.
- 쓰레드 락 Acquire/Release
- 파일 open/close
- 데이터베이스 시작 후 에러 유무에 따라 롤백/커밋
-

파일 삭제 등의 처리는 예외가 발생할 수 있기 때문에 예외 처리가 필요하다
다른 프로그래밍 언어에서도 다음과 같은 방법으로 처리한다
"""

def process(fd):
    # do something
    print('processing ...')

fd = open('test.txt')
try:
    print('start of process')
    process(fd)
finally:
    fd.close()
    print('end of process')

"""
하지만 아래와 같은 경우가 훨씬 파이썬스럽다
"""
print('test with !!!')
with open('test.txt') as fd:
    process(fd)

"""
https://peps.python.org/pep-0343/
작동 방식을 풀어서 설명하면 다음과 같다

# naive approach
VAR = EXPR
VAR.__enter__()
try:
    BLOCK
finally:
    VAR.__exit__()

# pythonic approach    
with VAR = EXPR:
    BLOCK1

# more pythonic using as keyword
with EXPR as VAR:
    BLOCK1
"""

"""
with 문은 컨텍스트 관리자로 진입하게 한다. 이는 __enter__와 __exit__ 메소드를 가진 객체를 대상으로 이루어지며
__enter__ 메소드는 컨텍스트 관리자가 진입할 때 호출되고
__exit__ 메소드는 컨텍스트 관리자가 종료될 때 호출된다.
또한, __enter__에서 return 된 값이 with 문의 as 뒤에 오는 변수에 할당된다.
반드시 그럴 필요는 없지만, 무언가 반환하는 것은 좋은 습관이다.
(컨텍스트 관리자를 구현하는 것은 매직 메서드 두 개면 된다.)

그리고 __exit__에서는 특별한 작업이 없다면 아무것도 반환하지 않아도 된다. 예외 유무에 따라 True/False를 반환한다.
True를 반환하면 잠재적으로 발생한 예외를 호출자에게 전파하지 않고 멈춘다는 의미이다. 
exit은 블록에서 발생한 예외를 파라미터로 받게 된다. 예외가 없다면 None이 들어온다. 오류를 조용히 무시하는 것은
굉장히 나쁜 습관임을 기억해야한다.
True로 반환할 때는 정말 특별한 이유가 있어야한다. 대부분의 경우에는 False를 반환하고 예외를 처리하는 것이 좋다.

Practical한 usecase를 살펴보는 것은 이 페이지의 범위를 벗어나므로, 작동 방식만 이해해보자

"""

print('my process test !!!')
class Process:
    name = 'Custom_Process_no_1'
    def __enter__(self):
        print('start of process')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('end of process')

with Process() as p:
    print(f'processing {p.name} ...')

# contextlib 모듈을 이용한 구현
# yield 이전이 __enter__, 이후가 __exit__ 역할을 수행한다.
# 장점 1: 컨텍스트 관리자를 구현하는 클래스를 정의하지 않아도 된다.
# 장점 2: 기존 함수를 리팩토링하기 쉬워진다.
#   특정 객체에 속하지 않는 컨텍스트 관리자가 필요한 경우 좋다.
#   이를 객체지향적으로 설계하려면 아무 의미 없는 가짜 부모클래스를 만들어야하는 번거로움이 있다

# contextmanager 데코레이터를 이용한 구현
# 1. 제너레이터 함수를 정의하고
# 2. yield를 이용해 컨텍스트 관리자가 진입할 때 반환할 값을 지정하고
# 3. yield 이후에는 컨텍스트 관리자가 종료될 때 실행할 코드를 작성한다.

print('my gen process test !!!')
from contextlib import contextmanager

@contextmanager
def gen_process():
    print('start of process')
    yield 'gen_process'
    print('end of process')

with gen_process() as gp:
    print(f'processing {gp} ...')


# ContextDecorator 클래스 활용
# ContextDecorator는 믹스인 클래스이다 -> 데코레이터를 적용하기 위한 로직을 제공
print(f'start Conext Decorator test !!!')
from contextlib import ContextDecorator

class process_decorator(ContextDecorator):
    def __enter__(self):
        print('start of process')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('end of process')

@process_decorator()
def process():
    print('processing ...')

process()
# 이젠 process를 여러번 호출해도 좋다
# 또한, with 문을 사용하지 않아도 된다
# 함수를 래핑하는 데코레이터를 사용했으므로 그저 함수만 호출하면 된다
# 또한 process 함수와 process_decorator 데코레이터 사이의 독립성이 보장된다
# 서로가 독립적으로 접근 및 관여 불가 -> 매우 좋은 특성이다
process()

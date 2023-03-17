# 테스트용 시퀀크 클래스
class MySequence:
    def __init__(self):
        ...

    # [item]로 접근시 호출되는 매직 메서드
    def __getitem__(self, item):
        item_type = type(item)
        print(f'{item} is {item_type} type')

        if item_type == int:        # 정수가 들어오면 인덱싱
            print(f'implement sequence indexing here')

        elif item_type == slice:    # 슬라이스가 들어오면 슬라이싱
            print(f'implement sequence slicing here')

        else:   # 그 이외의 타입은 일단 예외처리
            raise ValueError('Unhandled type for either indexing and slicing')

    def __len__(self):
        ...


seq = MySequence()


# seq[1]        #
# seq[:3]
# seq['hi']


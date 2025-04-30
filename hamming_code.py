def hamming_code(hcode):
    hcode = list(hcode)
    n = len(hcode)
    error_position = 0

    # 패리티 비트 위치 : 1, 2, 4, 8, 16 .....
    i = 0
    while (1 << i) <= n:
        idx = (1 << i) - 1
        count = 0

        # 해당 패리티 비트가 검사하는 비트들의 합 계산
        for j in range(idx, n, 2*(idx+1)):
            count += sum(int(hcode[k]) for k in range(j, min(j+idx+1, n)))
        if count % 2 != 0:
            error_position += idx + 1
        i = i + 1
        # 오류가 있으면 해당 비트 반전
    if error_position != 0 and error_position <= n:
        hcode[error_position - 1] = '0' if hcode[error_position - 1] == '1' else '1'

    return ''.join(hcode)

# ex) 111101001010 -> stay
# ex) 0011011 -> 0011001
input_code = input("Input hamming code(binary) : ")
print(f"Before : {input_code}\nAfter correction : {hamming_code(input_code)}")

# print(1 << 0)
# print(1 << 1)
# print(1 << 2)
# print(1 << 3)
# print(1 << 4)
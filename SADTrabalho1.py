def solution(S):
    substring = ''

    
    if S:
        for i in S:
            
            if i == '{':
                substring += '}'
            if i == '[':
                substring += ']'
            if i == '(':
                substring += ')'

            
            if i == '}':
                if substring.endswith('}'):
                    substring = substring[:-1]
                else:
                    return 0
            if i == ']':
                if substring.endswith(']'):
                    substring = substring[:-1]
                else:
                    return 0
            if i == ')':
                if substring.endswith(')'):
                    substring = substring[:-1]
                else:
                    return 0

        
        if substring:
            return 0
        else:
            return 1
    else:
        return 0


S = 'cenas'
print(solution(S))

S = 'teste]]'
print(solution(S))

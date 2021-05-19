import collections


def remove_duplicate_chr(s):
    stack = []
    seen = set()
    cnt = collections.Counter(s)

    for character in s:
        if character not in seen:
            while stack and character < stack[-1] and cnt[stack[-1]] > 0:
                seen.discard(stack.pop())
            seen.add(character)
            stack.append(character)
        cnt[character] -= 1
    return ''.join(stack)


if __name__ == '__main__':
    s = 'bcac'
    print(remove_duplicate_chr(s))
# takes O(n²) time
def reverse(s: str) -> str:
    if len(s) > 0:
        string = ''
        s_arr = s.split(' ')[::-1]

        for word in s_arr:
            for letter in word[::-1]:
                string += letter

            string += ' '

        return string

    return ''


print(reverse('Hi my name is Andrei'))

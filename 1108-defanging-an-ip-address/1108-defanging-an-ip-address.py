class Solution(object):
    def defangIPaddr(self, address):
        result = []
        for ip in address:
            if ip == '.':
                result.append("[.]")
            else:
                result.append(ip)
        return "".join(result)            
class Solution(object):
    def maskPII(self, s):
        if '@' in s:
            # Email
            name, domain = s.lower().split('@')

            return name[0] + '*****' + name[-1] + '@' + domain

        # Phone number
        digits = ''.join(c for c in s if c.isdigit())

        local = '***-***-' + digits[-4:]

        if len(digits) == 10:
            return local

        country = len(digits) - 10
        return '+' + '*' * country + '-' + local
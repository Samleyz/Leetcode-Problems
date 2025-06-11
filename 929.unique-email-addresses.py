class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        mails = set()
        st = ''
        seen = set()
        for i in emails:
            for j in i:
                seen.add(j)
                if '@' not in seen:
                    if j == '.':
                        continue
                    else:
                        if j == '+':
                            seen.add('+')
                        elif '+' in seen:
                            continue
                        else:
                            st+=j


                else:
                    st +=j

            
            mails.add(st)
            st = ''
            seen = set()
        return len(mails)

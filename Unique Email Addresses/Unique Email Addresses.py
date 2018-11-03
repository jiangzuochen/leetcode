class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # emailsSet = set()
        return len(set([x.split('@')[0].split('+')[0].replace('.','') \
                        +'@'+ x.split('@')[1] for x in emails]))
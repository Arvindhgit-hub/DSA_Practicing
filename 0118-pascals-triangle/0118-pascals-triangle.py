class Solution(object):
    def generate(self, numRows):
        resRow = [[1]]
        preRow = resRow[-1]     
        for i in range(numRows-1):
            preRow = resRow[-1] 
            newRow = [1]
            for j in range(len(resRow[-1])-1):
                newRow.append(preRow[j]+preRow[j+1])
            newRow.append(1)
            resRow.append(newRow)
        return resRow

                

              

  
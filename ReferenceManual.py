def num_corresponding_to_maj_min_color(MAJOR_COLORS,MINOR_COLORS):
         mappingTable = {}
         num = 1
         for i in MAJOR_COLORS:
            for j in MINOR_COLORS:
               print(num,i,j)
               mappingTable[num] = i + " " + j
               num=num+1
         
           displayMappingTable(mappingTable)
             
                

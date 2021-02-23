def num_corresponding_to_maj_min_color(MAJOR_COLORS,MINOR_COLORS):
         mapping = {}
         num = 1
         for i in MAJOR_COLORS:
            for j in MINOR_COLORS:
               print(num,i,j)
               mapping[num] = i + ' ' + j
               num=num+1
             
                

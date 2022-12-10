"""
初始映射  line 360 start='Atom type, charge, xyz'
        end = 两空行 和 Bonds
        
        
健   line 76 start = 'Bond Coeffs'
    end = 两空行 Angle Coeffs
    
    line 551 start= 'Bonds'
    end = 1 空行 + Angles
    

角   line 128 start= Angle Coeffs
    end= 两空行 + dihedral coeffs

    line 750 start = Angles
    end = 两空行 + Dihedrals
    
二面角     line 216 start= dihedral coeffs
            end = 两空行+ Atom type, charge, xyz

          line 1119 start = Dihedrals
          end = end

"""
def is_break_time(content_line):
    """
    判断何时break，尝试将第一个字符转为 int
    若不能转换， 则表示应该退出
    """
    try:
        int(content_line[0])
        return False
    except:
        return True


# 简单起见，多读取几次，省的计算优先级，并且兼容性更好

def get_origin_map():
    with open('y6.txt', encoding='utf-8', mode='r') as file:
        content_line_list = file.readlines()
        origin_map_id_to_type = {}
        times = 0

        for content_line in content_line_list:
            if 'Atom' in content_line and 'type' in content_line and 'charge' in content_line and 'xyz' in content_line:
                print('Find!!!!!!!!!!')
                index = content_line_list.index(content_line)
                new_list = content_line_list[index+1:]
                for new_line in new_list:
                    if not new_line:
                        continue
                    if is_break_time(content_line=new_line):
                        break

                    new_one_line_list = new_line.split('	')
                    atom_id = new_one_line_list[0]
                    atom_type = new_one_line_list[2]
                    origin_map_id_to_type[atom_id] = atom_type
                    times = times + 1
                break
    return origin_map_id_to_type, times


map_d, times = get_origin_map()
print(map_d)

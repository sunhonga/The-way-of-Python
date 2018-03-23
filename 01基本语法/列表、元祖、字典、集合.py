# Author：SUN HONG
'''
  列表：
      申明列表：
               numbers1=[111,222,444]  numbers2=[888,999]  numbers3=[]
      添加元素：在列表最后增加元素：numbers1.append("555")
                在列表任意位置添加元素：numbers1.insert(2,"333")#表示在index为2的位置添加元素"333"
                合并两个列表：numbers1.extend(numbers2)
      删除元素：删除某个元素：del numbers1[2]
                删除整个列表：del numbers1
                删除最后一个元素：numbers1.pop()
                删除具体内容的那个元素：numbers1.remove("444")
      改变元素：numbers1[0]="aaa"
      排序列表：将列表逆置 numbers1.reverse()
      列表元素的统计：numbers1.count("555") 返回"555"出现的个数
                     numbers1.index("555") 返回"555"的index的值
      判断某个元素是否在列表： 100 in numbers1  返回为Flase
  元祖：()内置函数 count index
  字典：stus={'age':30,'name':'sunhong','sex':'nan'}
      新增 stus['address']='beijing'
      判断 'name' in stus 返回值为True
      删除 del stus['sex']   删除整个字典 del stus
      字典内置函数：len()获得字典长度，keys()获得字典键的列表，values（）获得字典值的列表
  集合：set()两个功能：去重 list_1=[1,6,7,4,1,2,6]
                           list_1=set(list_1)   list_1的数据类型为集合set
                      关系测试 list_2=[4,20,8,56,6]
                           list_1.intesrsection(list_2)   list_1&list_2取出交集｛4，6｝
                           list_1.union(list_2)           list_1|list_2取并集｛｝
                           list_1.difference(list_2)      list_1-list_2 取差集｛｝list_1中有的元素，list_2中没有
                                                          list_1^list_2 对称差集  在list_1或list_2中，但不会同时出现在二者中。


'''
# sort和reverse未解决
#b=[1,2,3,5,4]
#print(b.sort())   打印为None
b=[1,5,3,4]
a=b.index(5)
print(a)


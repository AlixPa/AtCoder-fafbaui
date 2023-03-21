def range_base_N(start,end,base,step=1):
  def Convert(n,base):
    string = "0123456789ABCDEF"
    if n < base:
      return string[n]
    else:
      return Convert(n//base,base) + string[n%base]
  return (Convert(i,base) for i in range(start,end,step))
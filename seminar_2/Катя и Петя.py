from math import sqrt
s, p = map( int, input('s, p = ').split() )
z = sqrt( (s/2)**2 - p )
print( int( s/2 - z ), int( s/2 + z ) )

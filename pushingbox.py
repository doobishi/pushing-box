class DFSp :
    def __init__( self, row, column, map ) :
        self.row = row
        self.column = column
        self.dungeon = map
        self.shorteststep = 1601
        self.totalpathfromptob = list()
        # print ( dungeon )
    # end constructor

    def reset ( self ) :
        self.dungeon = []
        self.shortestfromptob = []
        self.shorteststep = 1601

    def moveE( self, stX, stY ) :
        nextX = stX + 1
        nextY = stY 
        if ( nextY < self.row  and nextX < self.column ) :
            if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                return True
            else :
                return False
        else :
            return False
    # moveE

    def moveN( self, stX, stY ) :
        nextX = stX 
        nextY = stY - 1
        if ( nextY >= 0 ):
            if ( nextY < self.row  and nextX < self.column ) :
                if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                    return True
            return False
    # moveN
    def moveS( self, stX, stY ) :
        nextX = stX 
        nextY = stY + 1
        if ( nextY < self.row  and nextX < self.column ) :
            if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                return True

        return False
    # moveS

    def moveW( self, stX, stY ) :
        nextX = stX - 1
        nextY = stY 
        if ( nextX >= 0 ) :
            if ( nextY < self.row  and nextX < self.column ) :
                if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                    return True
            return False
    # moveW
        
    def routeFrompersonToboxfront( self, perX, perY, boxX, boxY, step, path ) : # return per to box shortest path
        if ( perX == boxX and perY == boxY ) :
            # recored
            # print ( "append", [ perX , perY ]  )
            path.append( [ perX , perY ] )
            # print ( path )
            temp = path[0:]
            self.totalpathfromptob.append ( temp )
            # print ( "pop")
            path.pop() 
            # print ( path )
            return step
        else :
            pathOne = pathTwo = pathThr = pathFour = 1601
            self.dungeon[ perY ][ perX ] = 7
            # print ( "append", [ perX , perY ]  )
            path.append( [ perX , perY ] )
            # print ( path )
            # print ( path )
            # print(  "per :" , perX, perY )
            if ( self.moveE( perX, perY ) ) :
                step += 1
                perX += 1            
                # print( "eperX, perY, boxX, boxY =", perX, perY, boxX, boxY )
                self.dungeon[ perY ][ perX ] = 7
                pathOne = self.routeFrompersonToboxfront( perX, perY, boxX, boxY, step, path )
                # print ( "1pop")
                # # path.pop()
                # print ( path )
                self.dungeon[ perY ][ perX ] = 0
                perX -= 1
                step -= 1
                
            # print(  "reper :" , perX, perY )  
            if ( self.moveN( perX, perY ) ) :
                step += 1
                perY -= 1            
                # print( "nperX, perY, boxX, boxY =", perX, perY, boxX, boxY )
                self.dungeon[ perY ][ perX ] = 7
                pathTwo = self.routeFrompersonToboxfront( perX, perY, boxX, boxY, step, path )
                # print ( "2pop")
                # path.pop()
                # print ( path )
                self.dungeon[ perY ][ perX ] = 0
                perY += 1
                step -= 1
                
            # print(  "reper :" , perX, perY )    
            if ( self.moveS( perX, perY ) ) :
                step += 1
                perY += 1         
                # print( "sperX, perY, boxX, boxY =", perX, perY, boxX, boxY )
                self.dungeon[ perY ][ perX ] = 7
                pathThr = self.routeFrompersonToboxfront( perX, perY, boxX, boxY, step, path )
                # print ( "3pop")
                # path.pop()
                # print ( path )
                self.dungeon[ perY ][ perX ] = 0
                perY -= 1
                step -= 1
               
            # print(  "reper :" , perX, perY )  
            if ( self.moveW( perX, perY ) ) :
                step += 1
                perX -= 1
                # print( "wperX, perY, boxX, boxY =", perX, perY, boxX, boxY )
                self.dungeon[ perY ][ perX ] = 7
                pathFour = self.routeFrompersonToboxfront( perX, perY, boxX, boxY, step, path )
                # print ( "4pop")
                # path.pop()
                # print ( path )
                self.dungeon[ perY ][ perX ] = 0
                perX += 1
                step -= 1
            
            path.pop()
            return min( pathOne, pathTwo, pathThr, pathFour ) 
        # end else
    # routeFrompersonTobox  

    def setboxstloc( self, px, py, bx ,by ) :
        self.dungeon[ py ][ px ] = 7
        self.dungeon[ by ][ bx ] = 2

    def reboxstloc( self, px, py, bx ,by ) :
        self.dungeon[ py ][ px ] = 0
        self.dungeon[ by ][ bx ] = 0
    
    def totalpathfromptobclear( self ) :
        self.totalpathfromptob.clear()

    def shortestfromptob( self ) :
        index = 0
        min = 0
        while ( index < len( self.totalpathfromptob ) ) :
            if ( len ( self.totalpathfromptob[ min ] ) > len ( self.totalpathfromptob[ index ] ) ) :
                min = index 
            index += 1
       
        
        return self.totalpathfromptob[ min ]

class DFSb :
    def __init__( self, row, column, map, person ) :
        self.row = row
        self.column = column
        self.dungeon = map
        self.per = person 
        self.shorteststep = 1601
        self.totalformSTtoDes = list()
        self.shortestpath = [] 
        # print ( dungeon )
    # end constructor

    def reset( self ) :
        self.totalformSTtoDes.clear()
        self.shortestpath.clear() 
        self.shorteststep = 1601 
        self.dungeon.clear() 
        self.per.reset() 

    def moveE( self, stX, stY ) :
        nextX = stX + 1
        nextY = stY 
        if ( nextY < self.row  and nextX < self.column ) :
            if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                return True
            else :
                return False
        else :
            return False
    # moveE

    def moveN( self, stX, stY ) :
        nextX = stX 
        nextY = stY - 1
        if ( nextY >= 0 ):
            if ( nextY < self.row  and nextX < self.column ) :
                if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                    return True
            return False
    # moveN

    def moveS( self, stX, stY ) :
        nextX = stX 
        nextY = stY + 1
        if ( nextY < self.row  and nextX < self.column ) :
            if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                return True

        return False
    # moveS

    def moveW( self, stX, stY ) :
        nextX = stX - 1
        nextY = stY 
        if ( nextX >= 0 ) :
            if ( nextY < self.row  and nextX < self.column ) :
                if ( self.dungeon[ nextY ][ nextX ] == 0 or self.dungeon[ nextY ][ nextX ] == 9 ) :
                    return True
            return False
    # moveW


    def checkboxfront( self, x , y ):
        if ( x < 0 or y < 0 ):
            return False
        elif( x > self.column - 1 or y > self.row - 1   ) :
            return False 
        elif ( self.dungeon[ y ][ x ] == 5 ):
            return False
        else :
            return True

    
    def pushingbox( self, boxX, boxY, perX, perY, targetX, targetY, step, path ) :
        if ( step > self.shorteststep ) :
            return 1601
        else :
            if ( boxX == targetX and targetY == boxY ) :
                if ( self.shorteststep >= step ) :
                    self.shorteststep = step
                    # print ( "append" , [ boxX, boxY ] )
                    path.append( [ boxX, boxY ] )
                    temp = path[0:]
                    # print ( "su" , temp )
                    self.totalformSTtoDes.append( temp )
                    # print ( "pop" )
                    path.pop()
                    # print ( path )
                return step
            else :
                self.dungeon[ boxY ][ boxX ] = 7
                pathboxOne = pathboxTwo = pathboxThr = pathboxFour = 1601
                pOne = pTwo = pThr = pFour = 1601 
                reperX = perX
                reperY = perY
                ppathOne = []
                ppathTwo = []
                ppathThr = []
                ppathFour = []
                path.append( [ boxX, boxY ] )
                if ( self.moveE( boxX, boxY ) ) :
                    if ( self.checkboxfront( boxX - 1, boxY ) ) :
                        person.setboxstloc( perX, perY, boxX, boxY )
                        pOne = person.routeFrompersonToboxfront( perX, perY, boxX - 1, boxY, 0, ppathOne ) 
                        person.reboxstloc( perX, perY, boxX, boxY )
                        ppathOne.clear() 
                        if ( pOne != 1601 ) :
                            ppathOne = person.shortestfromptob()
                            person.totalpathfromptobclear()
                            perX = boxX 
                            perY = boxY
                            step += 1
                            boxX += 1 
                            self.dungeon[ boxY ][ boxX ] = 7
                            # print ( " path append ", ppathOne )
                            path.append( ppathOne )
                            # print ( path )
                            pathboxOne = self.pushingbox( boxX, boxY, perX, perY, targetX, targetY, step, path )               
                            # print ( "pop" )
                            path.pop()
                            # print ( path )
                            self.dungeon[ boxY ][ boxX ]  = 0
                            boxX -= 1
                            step -= 1
                            perX = reperX
                            perY = reperY
                

                if ( self.moveN( boxX, boxY ) ) :
                    if ( self.checkboxfront( boxX , boxY + 1 ) ) :
                        # print ( " box can N =",boxX, boxY )
                        person.setboxstloc( perX, perY, boxX, boxY )
                        pTwo = person.routeFrompersonToboxfront( perX, perY, boxX, boxY + 1, 0, ppathTwo )
                        person.reboxstloc( perX, perY, boxX, boxY )
                        ppathTwo.clear()
                        if ( pTwo != 1601 ) :
                            ppathTwo = person.shortestfromptob()
                            person.totalpathfromptobclear()
                            perX = boxX
                            perY = boxY
                            boxY -= 1
                            step += 1
                            self.dungeon[ boxY ][ boxX ]  = 7
                            # print ( "append", ppathTwo )
                            path.append( ppathTwo )
                            # print ( path )
                            pathboxTwo = self.pushingbox( boxX, boxY, perX, perY, targetX, targetY, step, path )
                            # print ( "pop" )
                            path.pop()
                            # print ( path )
                            # path.pop()
                            self.dungeon[ boxY ][ boxX ]  = 0
                            boxY += 1
                            step -= 1
                            perX = reperX
                            perY = reperY

                
                if ( self.moveS( boxX, boxY ) ) :
                    if ( self.checkboxfront( boxX , boxY - 1 ) ) :
                        # print ( " box can S =",boxX, boxY )
                        person.setboxstloc( perX, perY, boxX, boxY )
                        pThr = person.routeFrompersonToboxfront( perX, perY, boxX, boxY - 1, 0, ppathThr )
                        person.reboxstloc( perX, perY, boxX, boxY )
                        ppathThr.clear()
                        if ( pThr != 1601 ) :
                            ppathThr = person.shortestfromptob()
                            person.totalpathfromptobclear()
                            perX = boxX
                            perY = boxY
                            boxY += 1
                            step += 1          
                            self.dungeon[ boxY ][ boxX ]  = 7
                            # print( "append", ppathThr )
                            path.append( ppathThr )    
                            # print ( path )      
                            pathboxThr = self.pushingbox( boxX, boxY, perX, perY, targetX, targetY, step, path )
                            # print ( "pop" )
                            path.pop()
                            # print ( path )
                            # path.pop()
                            self.dungeon[ boxY ][ boxX ]  = 0
                            boxY -= 1
                            step -= 1
                            perX = reperX
                            perY = reperY
                
                
                if ( self.moveW( boxX, boxY ) ) :
                    if ( self.checkboxfront( boxX + 1 , boxY ) ) :
                        person.setboxstloc( perX, perY, boxX, boxY )
                        pFour = person.routeFrompersonToboxfront( perX, perY, boxX + 1, boxY, 0, ppathFour )
                        person.reboxstloc( perX, perY, boxX, boxY )
                        ppathFour.clear()
                        if ( pFour != 1601 ) :
                            ppathFour = person.shortestfromptob()
                            person.totalpathfromptobclear()
                            perX = boxX
                            perY = boxY
                            boxX -= 1
                            step += 1
                            self.dungeon[ boxY ][ boxX ]  = 7
                            # print ( "append" , ppathFour ) 
                            path.append( ppathFour )
                            # print( path )
                            pathboxFour = self.pushingbox( boxX, boxY, perX, perY, targetX, targetY, step, path )
                            # print ( "pop " )
                            path.pop()
                            # print ( path )
                            # path.pop()
                            self.dungeon[ boxY ][ boxX ]  = 0
                            boxX += 1
                            step -= 1
                            perX = reperX
                            perY = reperY
        
                path.pop()
                return min( pathboxOne, pathboxTwo, pathboxThr, pathboxFour )
            # end else
    # pushingbox

    def setminmoveboxandper( self ) :
        index = 0
        min = 0
        while ( index < len ( self.totalformSTtoDes ) ) :
            if ( len( self.totalformSTtoDes[min] ) > len ( self.totalformSTtoDes[ index ] ) )  :
                min = index 
            index += 1
        self.shortestpath = self.totalformSTtoDes[ min ]

    def printmove( self ) :
        index = 0 
        while ( index + 2 < len( self.shortestpath ) ) :
            boxloc = self.shortestpath[ index ]
            # print ( boxloc )
            indexper = 0
            # print( " len=",  self.shortestpath[ index + 1 ] )
            while( indexper + 1 < len( self.shortestpath[ index + 1 ] ) ) :

                # print ( " indexper =", indexper )
                perloc = self.shortestpath[ index + 1 ][ indexper ]
                pernext = self.shortestpath[ index + 1 ] [ indexper + 1 ]
                # print ( " perlocnext", perloc , pernext )
                
                if ( pernext[0]  ==  perloc[0]  ) :
                    if ( pernext[1] == perloc[1] + 1 ):
                        print( "s" , end= "" )
                    else :
                        print ( "n", end = "" )
                else :
                    if ( pernext[0] == perloc[0] + 1 ) :
                        print( "e", end = "" )
                    else :
                        print ( "w", end = "" )
                
                indexper += 1
            # end whlie 


            boxnext = self.shortestpath[ index + 2 ]
            # print ( boxnext, boxloc  )
            if ( boxnext[0] == boxloc[0] ) :
                if ( boxnext[1] == boxloc[1] + 1 ):
                    print( "S", end = "" )
                else :
                    print ( "N", end = "" )
            else :
                if ( boxnext[0] == boxloc[0] + 1 ) :
                    print( "E", end = "" )
                else :
                    print ( "W", end = "" )
            
            index += 2
        print ( "  " )
#end class
    

# main
filedata = list()
filedataindex = 0
print( "cin file name input555.txt cin input555" )
strfile = input()
txtstr = ".txt"
strfile += txtstr
with open( strfile, 'r' ) as inputfile :
    for line_list in inputfile.readlines() :
        filedata.append( line_list )

row, column = [ int ( val ) for val in filedata[ filedataindex ].split() ] 
stop = False
while ( row != 0 and column != 0 ) :
    filedataindex += 1
    print( row, column )

    dungeon = []
    for i in range ( row ) :
        dungeon.append( [] )
    # for
    
    for i in range ( row ) :
        # print( "file=", filedata[ filedataindex ] )
        dungeon[i] = filedata[ filedataindex ][ 0 : column ]
        filedataindex += 1
    #for
    # print( "ii", filedataindex )

    map = []
    mapcopy = []
    for i in range ( row ) :
        map.append( [] )
        mapcopy.append([])

    px = py = bx = by = tx = ty = 0
    ir = 0
    ic = 0
    for ir in range( row ):
        for ic in range( column ) :
            str = dungeon[ ir ][ ic ]
            if ( str == ".") :
                map[ ir ].append( 0 )
                mapcopy [ ir ].append( 0 )
            elif( str == "S" ) :   
                 py = ir
                 px = ic 
                 map[ ir ].append( 0 )
                 mapcopy[ ir ].append( 0 )
            elif(str == "B" ):
                by = ir
                bx = ic
                map[ ir ].append( 0 )
                mapcopy[ ir ].append( 0 )
            elif ( str == "#" ):
                map[ ir ].append( 5 )
                mapcopy[ ir ].append( 5 )
            elif( str == "T" ) :
                ty = ir
                tx = ic
                map[ ir ].append( 9 )
                mapcopy[ ir ].append( 9 )

        
    person = DFSp( row, column, map )
    box = DFSb( row, column, mapcopy, person )
    step = 0
    path = list()
    # print( bx, by, px, py, tx, ty )
    step = box.pushingbox( bx, by, px, py, tx, ty, step, path )
    if ( step != 1601 ) :
        print( "========= " )  
        box.setminmoveboxandper()   
        box.printmove() 
    else :
        print ( "fail to des ")

    row, column = [ int ( val ) for val in filedata[ filedataindex ].split() ] 
    dungeon.clear()
    map.clear()
    mapcopy.clear() 
    path.clear() 
    person.reset()
    box.reset()






// Last updated: 8/5/2025, 2:55:46 PM

bool isRobotBounded(char * instructions){
    
    int direction = 0, x = 0, y = 0;  
    //N = 0, w= 1, s = 2, e= 3
   for (int i = 0 ; i < strlen(instructions); i++) {
        printf("%c\n ", instructions[i]);
        
        if (instructions[i] == 'L'){
            direction = (direction+1)% 4;
            printf("Left: %d\n ", direction);
        }
        else if (instructions[i] == 'R'){
            direction = (direction+3)% 4;    
            printf("Right: %d\n ", direction);
        }
        //apply the move
        else if (direction == 0){
            ++y;
        } 
        else if (direction == 1)
        {--x;}
        else if (direction == 2)
        {--y;}
        else{
            ++x;}
    }
    printf("x: %d y: %d", x, y);
  return direction !=0 || (x == 0 && y == 0);  //If north then never coming back or if the cordinates are equal to zero then fine
}

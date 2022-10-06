/* Objective function */
min: x2;

/* Variable bounds */


/*pomocna_mala -   1000b12 <=0;  */

b1_2=1;

/* 1 */
x1>=0;
y1>=0;
x1+13 <=666;
y1+ 5<=13;
x1+ 13 - 666 + 666b1_2 - x2<=0;
y1+ 5 - 13 + 13u1_2 - y2<=0;
/* 2 */
x2>=0;
y2>=0;
x2+10 <=666;
y2+ 7<=13;
x2+ 10 - 666 + 666b2_1 - x1<=0;
y2+ 7 - 13 + 13u2_1 - y1<=0;
u1_2+u2_1<=1;
b1_2+b2_1<=1;
b1_2+b2_1+u1_2+u2_1>=1;
u2_1+u1_2<=1;
b2_1+b1_2<=1;
b2_1+b1_2+u2_1+u1_2>=1;
int x1,x2,m,M;
int y1,y2;
bin u1_2,u2_1;
bin b1_2,b2_1;



int pomocna_mala,pomocna_velika;
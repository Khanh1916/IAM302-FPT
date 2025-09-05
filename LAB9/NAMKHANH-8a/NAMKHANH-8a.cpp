// NAMKHANH-8a.cpp : Defines the entry point for the console application.
 //
 /*
 #include <stdio.h>
 int i=1; // GLOBAL VARIABLE
 int main(int argc, char* argv[])
 {
 int j=2; // LOCAL VARIABLE
 printf("NAMKHANH-8a: %d %d\n", i, j);
 return 0;
 }
*/

#include <stdio.h>

int x = 10;    // Biến toàn cục x
int m = 20;    // Biến toàn cục m

int main() {
    int y = 30;    // Biến cục bộ y
    int n = 40;    // Biến cục bộ thứ hai

    printf("NAMKHANH %d %d %d %d", x, m, y, n);  // Thay "NAMKHANH" bằng tên của bạn
    return 0;
}
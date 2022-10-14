#include<bits/stdc++.h>
#include<iostream>
using namespace std;
void setZeroes(int matrix[][3]) {
  int rows = 3, 
  cols = 3;
  vector < int > dummy1(rows,-1), dummy2(cols,-1);
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (matrix[i][j] == 0) {
        dummy1[i] = 0;
        dummy2[j] = 0;
      }
    }

  }
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (dummy1[i] == 0 || dummy2[j]==0) {
        matrix[i][j] = 0;
      }
    }
  }

}

int main() {
  int arr[3][3]={1,1,1,1,0,1,1,1,1};
//  arr = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
  setZeroes(arr);
  cout<<"The Final Matrix is "<<endl;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      cout << arr[i][j] << " ";
    }
    cout << "\n";
  }
}

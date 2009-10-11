#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include "algo.h"

double **matralloc(int n, int m)
{
  double **matr = (double**)malloc(n*sizeof(size_t));
  int i;
  for(i=0;i<m;i++)
    matr[i] = (double*)malloc(m*sizeof(double));
  return matr;
}

void algo_normalize(double **matr, int n, int m)
{
  int i,j;
  double *lens = (double*)malloc(sizeof(double)*m);
  for(j=0;j<m;j++){
        double sum  = 0;
        int k;
        for(k=0;k<n;k++) sum+=matr[k][j]*matr[k][j];
        lens[j] = sqrt(sum);
  }
  for(i=0;i<n;i++)
    for(j=0;j<m;j++)
        matr[i][j] /=lens[j];
  free(lens);
}

main(){
  double test[][3] = {{1,2,3}, {1,2,3}};
  double **matr = matralloc(2,3);
  int i,j;
  for(i=0;i<2;i++)
    for(j=0;j<3;j++)
      *(*(matr+i)+j) = test[i][j];
  algo_normalize(matr, 2, 3);
  for(i=0;i<2;i++){
    for(j=0;j<3;j++){
      printf("%2.4f ", matr[i][j]);
    }
    printf("\n");
  }
}

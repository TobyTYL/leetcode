#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N_THREADS 100

int counter;

void *thread_code(void *arg)
{
    counter = counter + 1;
    pthread_exit(0);
}

void start_threads()
{
    int i;
    pthread_t threads[N_THREADS];
    counter = 0;
    for (i = 0; i < N_THREADS; i++)
    {
        pthread_create(&threads[i], NULL, thread_code, NULL);
    }
    for (i = 0; i < N_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }
    printf("Counter value: %d\n", counter);
}

int main()
{
    int i;
    int n = 100000;
    int pass_n = 0;
    for (i = 0; i < n; i++)
    {
        printf("Test %d: ", i + 1);
        start_threads();
        if (counter == N_THREADS)
        {
            pass_n++;
            printf("PASSED\n");
        }
        else
        {
            printf("FAILED\n");
        }
    }
    printf("Passed %d out of %d tests\n", pass_n, n);
    return EXIT_SUCCESS;
}

#include <stdio.h>
#include <stdlib.h>

#define MAX_PROCESOS 200   // por si quieren simular mas de 100

typedef struct {
    int id;   			// ID del proceso
    int arrival;                // Tiempo de llegada (t0, t1... tn)
    int burst;                  // Ráfaga de CPU original (tiempo cpu)
    int priority;               // Tiempo restante (para RR, SRTN)
    int remaining;		// Para algoritmos con prioridades
    int start_time;		// Primer instante en que se ejecuta
    int finish_time;		// Momento en que termina
    int waiting_time;		// Tiempo total de espera
    int turnaround;		// finish_time - arrival
    int response_time;          // primer instante en que el proceso recibe CPU − arrival
} Process;

int main(void) {
    Process procesos[MAX_PROCESOS];
    int n = 0;

    // Lee desde stdin hasta EOF: cada línea debe tener id arrival burst priority
    while (scanf("%d %d %d %d",
                 &procesos[n].id,
                 &procesos[n].arrival,
                 &procesos[n].burst,
                 &procesos[n].priority) == 4) {

        procesos[n].remaining    = procesos[n].burst;
        procesos[n].start_time   = -1;
        procesos[n].finish_time  = 0;
        procesos[n].waiting_time = 0;
        procesos[n].turnaround   = 0;
        procesos[n].response_time= -1;
        n++;

        if (n >= MAX_PROCESOS) {
            fprintf(stderr, "Se alcanzó el límite MAX_PROCESOS=%d\n", MAX_PROCESOS);
            break;
        }
    }

    printf("Se leyeron %d procesos:\n", n);
    for (int i = 0; i < n; i++) {
        printf("P%3d: arrival=%3d burst=%2d priority=%d\n",
               procesos[i].id,
               procesos[i].arrival,
               procesos[i].burst,
               procesos[i].priority);
    }

    // Aquí ya puedes llamar a tus funciones de simulación:
    //void simulate_fcfs(Process *p, int n);
    //void simulate_rr(Process *p, int n, int quantum);
    //void simulate_sjf(Process *p, int n);
    //void simulate_srtn(Process *p, int n);
    //void simulate_priority(Process *p, int n);

    return 0;
}

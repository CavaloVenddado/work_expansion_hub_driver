#define Kp 10.0f
#define Ki 0.5f
#define Kd 0.8f
#define Kf 8.0f
#define TICK_PER_ROT 537.7
#define TICK_PER_RADIANS TICK_PER_ROT/(2*3.1415)
#define WHEEL_RADIUS 0.048

//para todos que vierem depois de mim... os dois parametros abaixo (wheel separation width e length) nao sao a distancia de roda a roda, mas sim a metade desse
//valor. agora porque ta com um nome enganoso, nao sei... mas nao se voce estiver lendo isso, não cometa o mesmo erro que eu (ficar 1 mês tentando descobrir pq
// o robo nao gira direito, pra ver que esses valores sao, na verdade, da roda até o centro do robô)
#define WHEEL_SEPARATION_WIDTH 0.1835 //0.367
#define WHEEL_SEPARATION_LENGTH 0.168 //0.336

#define L_SUM 10
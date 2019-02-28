#ifndef GF_BRIDGEOUT_H
#define GF_BRIDGEOUT_H

typedef struct{
        unsigned  char*        log;
        unsigned  char*        anti_log;
        unsigned  char*        inv;
 }gfp_w8_log_ZOut;

extern gfp_w8_log_ZOut table_p_global;

void galois_w08_region_multiply_bridgeOut(  char * sptr,  int num, int size,  char* dptr, int add);

void galios_matrix_dotprod_bridgeOut(int k, int w, int *matrix_row,
                          int *src_ids, int dest_id,
                          char **data_ptrs, char **coding_ptrs, int size);

gfp_w8_log_ZOut get_w8_log_tables_bridgeOut();

#endif

#ifndef _LIBGARIB_FLA2_
#define _LIBGARIB_FLA2_ 1
#include <stdlib.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

void compress(const uint8_t *src, size_t src_length, uint8_t **dst, size_t *dst_length);

#ifdef __cplusplus
}
#endif

#endif
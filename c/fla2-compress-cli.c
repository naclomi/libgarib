#include <stdio.h>
#include <string.h>

#include "fla2.h"

int main(int argc, const char **argv) {
    FILE *src = fopen(argv[1], "rb");
    fseek(src, 0, SEEK_END);
    size_t src_len = ftell(src);
    fseek(src, 0, SEEK_SET);
    uint8_t *src_buf = malloc(src_len);
    fread(src_buf, 1, src_len, src);
    fclose(src);
    uint8_t *dst_buf = NULL;
    size_t dst_len = 0;
    compress(src_buf, src_len, &dst_buf, &dst_len);
    free(src_buf);

    size_t dst_name_len = strlen(argv[1]) + 5;
    char *dst_name = malloc(dst_name_len);
    strcpy(dst_name, argv[1]);
    strcat(dst_name, ".fla");
    FILE *dst = fopen(dst_name, "wb");
    fwrite(dst_buf, 1, dst_len, dst);
    fclose(dst);
    free(dst_buf);
    free(dst_name);
    return 0;
}
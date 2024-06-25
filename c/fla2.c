#include <string.h>
#include <stdio.h>

#include "fla2.h"

static const char *MAGIC_NUMBER_FLA = "FLA2";

void compress(const uint8_t *src, size_t src_length, uint8_t **dst, size_t *dst_length) {
    int dst_cursor = 0;
    uint8_t *buf = (uint8_t *) malloc(src_length);
    *dst = buf;

    for (int n=0; n<4; n++) {
        buf[dst_cursor++] = MAGIC_NUMBER_FLA[n];
    }
    *(uint32_t *)&buf[dst_cursor] = src_length;
    dst_cursor += 4;

    uint8_t *window = (uint8_t *) malloc(0x1000);
    memset(window, 0, 0x1000);
    int window_wr_cursor = 0;
    int window_initialized_cursor = 0;

    size_t read_cursor = 0;
    uint8_t done = 0;
    while(!done) {
        int cmd_byte_location = dst_cursor;
        buf[dst_cursor++] = 0;

        uint8_t cmd = 0;
        int cmd_bit = 0;
        for(; cmd_bit < 8; cmd_bit++) {
            uint8_t next_byte = src[read_cursor++];

            window[window_wr_cursor++] = next_byte;
            window_initialized_cursor = (window_initialized_cursor < window_wr_cursor) ? window_wr_cursor : window_initialized_cursor;
            window_wr_cursor &= 0xfff;

            int best_token_idx = -1;
            int best_token_length = -1;
            
            int search_cursor = (window_wr_cursor - 2) & 0xfff;

            while (((search_cursor - window_wr_cursor) & 0xfff) >= 1) { 
                if (search_cursor < window_initialized_cursor &&
                    window[search_cursor] == next_byte)
                {
                    // Build token
                    size_t src_cursor = read_cursor;
                    int local_window_wr_cursor = window_wr_cursor;
                    int window_rd_cursor = (search_cursor + 1) & 0xfff;
                    for (int i=0; i<16; i++) {
                        if (src_cursor >= src_length) {
                            break;
                        }
                        if (window_rd_cursor >= window_initialized_cursor) {
                            break;
                        }
                        uint8_t next_src_byte = src[src_cursor];
                        uint8_t next_window_byte = window[window_rd_cursor];
                        if (next_window_byte != next_src_byte) {
                            break;
                        }
                        window[local_window_wr_cursor++] = next_src_byte;
                        window_initialized_cursor = (window_initialized_cursor < local_window_wr_cursor) ? local_window_wr_cursor : window_initialized_cursor;
                        local_window_wr_cursor &= 0xfff;
                        window_rd_cursor = (window_rd_cursor + 1) & 0xfff;
                        src_cursor++;
                    }
                    int token_idx = search_cursor;
                    int token_length = (window_rd_cursor - search_cursor) & 0xfff;
                    if (token_length > best_token_length) {
                        best_token_idx = token_idx;
                        best_token_length = token_length;
                    }
                    if (((window_wr_cursor - search_cursor) & 0xFFF) <= token_length) {
                        break;
                    }
                }
                search_cursor = (search_cursor - 1) & 0xfff;
            }

            if (best_token_idx == -1 || best_token_length <= 2) {
                buf[dst_cursor++] = next_byte;
            } else {
                cmd |= 1 << (7-cmd_bit);

                int backref_start = (window_wr_cursor - 1 - best_token_idx) & 0xfff;
                int backref_len = (best_token_length - 2) & 0xF;
                uint16_t backref = ((backref_start & 0xFF) << 8) | ((backref_start & 0xF00) >> 4) | backref_len;

                
                *(uint16_t *)&buf[dst_cursor] = backref;
                dst_cursor += 2;

                read_cursor += backref_len + 1;
                window_wr_cursor = (window_wr_cursor + backref_len + 1) & 0xfff;
            }

            if (read_cursor >= src_length) {
                done = 1;
                // write mid-block terminator sequence, if necessary
                if (cmd_bit < 7) {
                    cmd |= 1 << (7-(cmd_bit+1));
                    buf[dst_cursor++] = 0;
                    buf[dst_cursor++] = 0;
                }
                break;
            }
        }

        buf[cmd_byte_location] = cmd;

        // write end-block terminator sequence, if necessary
        if (done && cmd_bit == 7) {
            buf[dst_cursor++] = 0x80;
            buf[dst_cursor++] = 0x00;
            buf[dst_cursor++] = 0x00;
        }
    }
    free(window);
    *dst_length = dst_cursor;
}


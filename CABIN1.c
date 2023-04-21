#include <stdio.h>
#include <string.h>
int main() {
    char sen[100];
    fgets(sen,100,stdin);
     
    int pc = 0, nc = 0;
    char word[20];
    int word_length = 0;
    
    for (int i = 0; i < strlen(sen); i++) {
        char c = sen[i];
        if (c == ' ' || c == '\t' || c == '\n') {
            if (word_length > 0) {
                word[word_length] = '\0';               
                if (strcmp(word, "happy") == 0 || strcmp(word, "great") == 0 || strcmp(word, "excellent") == 0) {
                    pc++;
                } else if (strcmp(word, "sad") == 0 || strcmp(word, "bad") == 0 || strcmp(word, "Terrible") == 0) {
                    nc++;
                }              
                word_length = 0;
            }
        } else {
            
            word[word_length++] = c;
        }
    }
    
    if (pc> nc) {
        printf("Positive");
    } else if (nc > pc) {
        printf("Negative");
    } else {
        printf("Neutral");
    }
    
    return 0;
}
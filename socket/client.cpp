#include <iostream>
#include <fstream>

// Network libs
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    (void)argc;
    // cria socket
    int sock = socket(AF_INET, SOCK_STREAM, 0); // IPV4

    sockaddr_in serverAddr{}; // Structure describing an Internet socket address
    serverAddr.sin_family = AF_INET; // familia de endereços IPV4
    serverAddr.sin_port = htons(8080);

    // Ip para binario
    inet_pton(AF_INET, argv[1], &serverAddr.sin_addr);

   
    connect(sock, (sockaddr*)&serverAddr, sizeof(serverAddr)); // socket, scoket adess e socket lenght

    std::ifstream file(argv[2], std::ios::binary); // abir o arquivo

    char buffer[1024];
    while (!file.eof()) {
        file.read(buffer, sizeof(buffer));
        send(sock, buffer, file.gcount(), 0);
    }

    close(sock);
    return 0;
}

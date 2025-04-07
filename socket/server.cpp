#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    int server = socket(AF_INET, SOCK_STREAM, 0);

    sockaddr_in address{};
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;   // aceita conexões de qualquer IP
    address.sin_port = htons(8080);         // porta 8080
    bind(server, (sockaddr*)&address, sizeof(address));

    // Fica ouvindo o server
    listen(server, 1);

    std::cout << "Aguardando conexão" << std::endl;

    socklen_t addrlen = sizeof(address);
    int client_socket = accept(server, (sockaddr*)&address, &addrlen); // Quando ouver conexão, ele aceita e cria um novo socket -> socket com o cliente que conetou

    std::cout << "Conexão estabelecida!" << std::endl;

    char buffer[1024];
    ssize_t bytesReceived;
    while ((bytesReceived = recv(client_socket, buffer, sizeof(buffer), 0)) > 0) { // le os dados do client e quanto tiver dados chegando ele fica aberto
        std::cout.write(buffer, bytesReceived);
    }

    close(client_socket);
    close(server);
    return 0;
}

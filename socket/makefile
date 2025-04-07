CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

.PHONY: all server client clean

all: server client

server: server.cpp
	$(CXX) $(CXXFLAGS) server.cpp -o server
	@echo "Servidor rodando"
	./server

client: client.cpp
	$(CXX) $(CXXFLAGS) client.cpp -o client
	@echo "Cliente executado."
	./client 127.0.0.1 msg.txt

clean:
	rm -f server client

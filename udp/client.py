import socket
import struct # empactor e desempactor pagotes de dados bionarios

def checksum(data: bytes) -> int:
    # Calcular o checksum
    
    if len(data) % 2 != 0: # check se for impar adiconar mais um byte no final pra encaixar no cojuunto de palavras de 16 bits
        data += b'\x00'
    
    soma = 0
    #  2 em 2 bytes
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        soma += word
        soma = (soma & 0xffff) + (soma >> 16)
    
    # inverter os bits -> (one's complement)
    return ~soma & 0xffff

def build_udp_packet(src_ip, dst_ip, src_port, dst_port, data):
    # ip para bytes
    src_ip_bytes = socket.inet_aton(src_ip)
    dst_ip_bytes = socket.inet_aton(dst_ip)

    # header = 8 bytes + msg
    udp_length = 8 + len(data)

    udp_header = struct.pack('!HHHH', src_port, dst_port, udp_length, 0) # -> checksum 0 por equanto

    placeholder = 0
    protocol = 17  # 17 = UDP
    pseudo_header = struct.pack('!4s4sBBH',
                                src_ip_bytes,
                                dst_ip_bytes,
                                placeholder,
                                protocol,
                                udp_length)

    # hecksum com pseudo-header + cabeçalho UDP + dados
    checksum_data = pseudo_header + udp_header + data
    udp_checksum = checksum(checksum_data)

    # atualizar o checksum
    udp_header = struct.pack('!HHHH',
                             src_port,
                             dst_port,
                             udp_length,
                             udp_checksum)

    return udp_header + data

def main():
    serve_ip = "127.0.0.1" 
    client_ip = "127.0.0.1"  
    server_port = 5555 
    client_port = 6565 
    
    msg = b"Mensagem Legal"

    # Monta o cabeçalho UDP + dados
    udp_packet = build_udp_packet(serve_ip, client_ip, server_port, client_port, msg)
    
    # desmontar o header pra verificar
    (source_port, dest_port, length, checksum) = struct.unpack('!HHHH', udp_packet[:8])

    print("UDP header")
    print("Porta de origem:", source_port)
    print("Porta de destino:", dest_port)
    print("Comprimento:", length)
    print(f"Checksun: 0x{checksum:04x}")
    
    payload = udp_packet[8:]
    print("paylioad: ", payload.decode('utf-8', errors='ignore'))

    # Socket por onde vai ser mandado a msg
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    sock.sendto(udp_packet, (client_ip, 0))
    print("Done")


if __name__ == "__main__":
    main()

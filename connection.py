import psycopg
import argparse
import time

def simulate_connections(dbname, user, password, host, port, num_connections, duration):
    connections = []
    try:
        for _ in range(num_connections):
            conn = psycopg.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            connections.append(conn)
            print(f"Connection {_+1} established")
        
        time.sleep(duration)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close all connections
        for conn in connections:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate database connections")
    parser.add_argument("--dbname", required=True, help="Name of the database")
    parser.add_argument("--user", required=True, help="Database user")
    parser.add_argument("--password", required=True, help="Password for the database user")
    parser.add_argument("--host", default="localhost", help="Database host")
    parser.add_argument("--port", default="5432", help="Database port")
    parser.add_argument("--num_connections", type=int, default=1, help="Number of connections to simulate")
    parser.add_argument("--duration", type=int, default=10, help="Duration to keep the connections open (in seconds)")
    
    args = parser.parse_args()
    
    simulate_connections(
        dbname=args.dbname,
        user=args.user,
        password=args.password,
        host=args.host,
        port=args.port,
        num_connections=args.num_connections,
        duration=args.duration
    )
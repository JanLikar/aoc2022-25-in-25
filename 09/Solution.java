import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Set;
import java.util.Vector;
import java.util.HashSet;


class Solution {
    static class Move {
        public Character direction;
        public int distance;

        public Move(Character direction, int distance) {
            this.direction = direction;
            this.distance= distance;
        }
    }

    static class Coordinates {
        public int x;
        public int y;

        Coordinates() {
            this.x = 0;
            this.y = 0;
        }

        Coordinates(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Coordinates applyMove(Move move) {
            switch(move.direction) {
                case 'U':
                    return new Coordinates(x, y + 1);
                case 'D':
                    return new Coordinates(x, y - 1);
                case 'L':
                    return new Coordinates(x - 1, y);
                case 'R':
                default:
                    return new Coordinates(x + 1, y);
            }
        }

        public Coordinates followHead(Coordinates head) {
            Boolean shouldMove = Math.abs(x - head.x) > 1 || Math.abs(y - head.y) > 1;
            
            if (!shouldMove) {
                return this;
            }

            Coordinates coordinates = new Coordinates(x, y);

            if(x > head.x) {
                coordinates.x--;
            }
            else if(x < head.x) {
                coordinates.x++;
            }

            if(y > head.y) {
                coordinates.y--;
            }
            else if(y < head.y) {
                coordinates.y++;
            }

            return coordinates;
        }

        @Override
        public int hashCode() {
            return x * 31 + y * 17;
        }

        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Coordinates))
                return false;
            if(obj.equals(null))
                return false;

            Coordinates other = (Coordinates) obj;
            return x == other.x && y == other.y;
        }
    }

    public static void main(String[] args) {
         Vector<Move> moves = new Vector<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));

            String line = null;  
            while ((line = reader.readLine()) != null)
            {  
                String[] parts = line.split(" ");
                Character direction = parts[0].charAt(0);
                int distance = Integer.parseInt(parts[1]);
                moves.add(new Move(direction, distance));
            }
            reader.close();
        }
        catch(Exception e) {
            System.out.println("Couldn't read the input.");
        }

        System.out.println(countVisited(moves));
        System.out.println(countVisited(moves, 9));
    } 

    private static int countVisited(Vector<Move> moves) {
        return countVisited(moves, 1);
    }

    private static int countVisited(Vector<Move> moves, int tailLength) {
        Set<Coordinates> visited = new HashSet<Coordinates>();
        Coordinates head = new Coordinates();
        Coordinates[] tail = new Coordinates[tailLength];

        for(int i = 0; i < tailLength; i++) {
            tail[i] = new Coordinates();
        }

        for(Move m : moves) {
            for(int i = 0; i < m.distance; i++) {
                head = head.applyMove(m);

                Coordinates neighbour = head;
                for(int j = 0; j < tailLength; j++) {
                    tail[j] = tail[j].followHead(neighbour);
                    neighbour = tail[j];
                }

                visited.add(tail[tail.length - 1]);
            }
        }

        return visited.size();
    }
}

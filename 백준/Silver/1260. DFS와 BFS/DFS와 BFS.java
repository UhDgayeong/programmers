import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Arrays;

public class Main {

    public static void bfs(int v, LinkedList<Integer>[] graph) {
        LinkedList<Integer> visited = new LinkedList<>();
        LinkedList<Integer> need_visited = new LinkedList<>();
        visited.add(v);

        Collections.sort(graph[v]);
        need_visited.addAll(graph[v]);
        while (!need_visited.isEmpty()) {
            int node = need_visited.poll();
            if (!visited.contains(node)) {
                visited.add(node);
                Collections.sort(graph[node]);
                need_visited.addAll(graph[node]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : visited) {
            sb.append(num + " ");
        }

        System.out.println(sb.toString().trim());
    }

    public static void dfs(int v, LinkedList<Integer>[] graph) {
        LinkedList<Integer> visited = new LinkedList<>();
        LinkedList<LinkedList<Integer>> need_visited = new LinkedList<>();
        visited.add(v);

        Collections.sort(graph[v]);
        need_visited.add(graph[v]);
        while (!need_visited.isEmpty()) {
            LinkedList<Integer> nodeList = need_visited.removeLast();

            if (nodeList.isEmpty()) {
                continue;
            }
            int node = nodeList.pop();
            if (!nodeList.isEmpty()) {
                need_visited.add(nodeList);
            }
            if (!visited.contains(node)) {
                visited.add(node);
                Collections.sort(graph[node]);
                need_visited.add(graph[node]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : visited) {
            sb.append(num + " ");
        }

        System.out.println(sb.toString().trim());
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String[] nmv = br.readLine().split(" ");
        int n = Integer.parseInt(nmv[0]);
        int m = Integer.parseInt(nmv[1]);
        int v = Integer.parseInt(nmv[2]);

        LinkedList<Integer>[] graph = new LinkedList[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new LinkedList<>();
        }

        for (int i = 0; i < m; i++) {
            String[] se = br.readLine().split(" ");
            int start = Integer.parseInt(se[0]);
            int end = Integer.parseInt(se[1]);

            graph[start].add(end);
            graph[end].add(start);
        }

        LinkedList<Integer>[] graphCopy = new LinkedList[n+1];
        for (int i = 0; i < n+1; i++) {
            graphCopy[i] = new LinkedList<>(graph[i]);
        }

        dfs(v, graphCopy);
        bfs(v, graph);

        bw.flush();

        br.close();
        bw.close();
    }
}
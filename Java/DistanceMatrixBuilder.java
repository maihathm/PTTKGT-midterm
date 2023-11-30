import java.util.ArrayList;
import java.util.List;

public class DistanceMatrixBuilder {

    public static List<List<Double>> buildDistanceMatrix(List<List<Double>> data) {
        // Tạo ma trận khoảng cách giữa các điểm trong dữ liệu.
        // Khoảng cách của 2 điểm được tính theo công thức Euclidean.

        int numRows = data.size();
        int numColumns = data.size();

        List<List<Double>> matrix = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Double> row = new ArrayList<>();
            for (int j = 0; j < numColumns; j++) {
                double distance = Math.sqrt(Math.pow(data.get(i).get(0) - data.get(j).get(0), 2)
                        + Math.pow(data.get(i).get(1) - data.get(j).get(1), 2));
                row.add(Math.round(distance * 100.0) / 100.0);
            }
            matrix.add(row);
        }

        return matrix;
    }

    public static void main(String[] args) {
        // Example usage
        List<List<Double>> inputData = new ArrayList<>();
        inputData.add(List.of(1.0, 2.0));
        inputData.add(List.of(3.0, 4.0));
        inputData.add(List.of(5.0, 6.0));

        List<List<Double>> distanceMatrix = buildDistanceMatrix(inputData);

        // In ma trận khoảng cách
        for (List<Double> row : distanceMatrix) {
            System.out.println(row);
        }
    }
}

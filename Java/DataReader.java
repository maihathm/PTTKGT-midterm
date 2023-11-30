import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DataReader {

    public static List<List<Double>> readDistanceMatrix(String filePath) {
        /**
         * Đọc một tệp dữ liệu chứa ma trận khoảng cách từ định dạng được chỉ định và trả về ma trận khoảng cách.
         * 
         * @param filePath Đường dẫn đến tệp dữ liệu chứa ma trận khoảng cách.
         * @return List<List<Double>> Ma trận khoảng cách giữa các điểm trong dữ liệu.
         * @throws IOException Nếu có lỗi khi đọc tệp.
         */

        // Khởi tạo ma trận khoảng cách
        List<List<Double>> distanceMatrix = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            // Đọc dữ liệu từ tệp và chuyển thành ma trận
            String line;
            int lineNumber = 0;
            while ((line = br.readLine()) != null) {
                // Bỏ qua dòng đầu tiên (tiêu đề, nếu có)
                if (lineNumber == 0) {
                    lineNumber++;
                    continue;
                }

                // Tách dữ liệu x và y bằng dấu tab
                String[] values = line.split("\t");
                double x = Double.parseDouble(values[0]);
                double y = Double.parseDouble(values[1]);

                // Khởi tạo dòng mới cho ma trận khoảng cách
                List<Double> row = new ArrayList<>();
                row.add(x);
                row.add(y);

                // Thêm dòng vào ma trận
                distanceMatrix.add(row);

                lineNumber++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // Tạo một đối tượng DistanceMatrixBuilder
        DistanceMatrixBuilder matrixBuilder = new DistanceMatrixBuilder();

        // Gọi phương thức buildDistanceMatrix từ đối tượng matrixBuilder
        List<List<Double>> matrix = matrixBuilder.buildDistanceMatrix(distanceMatrix);

        return matrix;
    }

    public static void main(String[] args) {
        // Example usage
        String filePath = "TSP-01.txt";
        List<List<Double>> distanceMatrix = readDistanceMatrix(filePath);

        System.err.println(distanceMatrix);
    }
}

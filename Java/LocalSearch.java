import java.util.Arrays;
import java.util.List;

public class LocalSearch {

    public static double distanceCalc(int[][] distanceMatrix, int[] cityTour) {
        /*
         * Tính tổng khoảng cách của một tour du lịch.
         *
         * Args: distanceMatrix: Ma trận khoảng cách giữa các thành phố. cityTour: Một
         * tour du lịch, được biểu diễn bằng một mảng các thành phố theo thứ tự tham
         * quan.
         *
         * Returns: Tổng khoảng cách của tour du lịch.
         */
        double distance = 0;
        for (int k = 0; k < cityTour.length - 1; k++) {
            int m = k + 1;
            int cityK = cityTour[k];
            int cityM = cityTour[m];
            distance += distanceMatrix[cityK - 1][cityM - 1];
        }
        return distance;
    }

    // Function: 2_opt
    public static int[] localSearch2Opt(int[][] distanceMatrix, int[] cityTour, int recursiveSeeding) {
        /*
         * Tìm kiếm cục bộ 2-opt để cải thiện tour du lịch.
         *
         * Args: distanceMatrix: Ma trận khoảng cách giữa các thành phố. cityTour: Một
         * tour du lịch, được biểu diễn bằng một mảng các thành phố theo thứ tự tham
         * quan. recursiveSeeding: Số lần lặp của thuật toán tìm kiếm cục bộ 2-opt. Nếu
         * `recursiveSeeding < 0`, thuật toán sẽ chạy cho đến khi không thể cải thiện
         * tour du lịch được nữa.
         *
         * Returns: Một tour du lịch được cải thiện, tổng khoảng cách tour du lịch được
         * cải thiện. Được biểu diễn bằng một mảng các thành phố theo thứ tự tham quan.
         */
        int count = (recursiveSeeding < 0) ? -2 : 0;
        int[] cityList = Arrays.copyOf(cityTour, cityTour.length);
        double distance = distanceCalc(distanceMatrix, cityList) * 2;

        while (count < recursiveSeeding) {
            int[] bestRoute = Arrays.copyOf(cityList, cityList.length);
            int[] seed = Arrays.copyOf(cityList, cityList.length);

            // Duyệt qua tất cả các cặp đoạn đường trong tour du lịch
            for (int i = 1; i < cityList.length - 2; i++) {
                for (int j = i + 1; j < cityList.length - 1; j++) {
                    // Hoán đổi hai đoạn đường đó và tính lại tổng khoảng cách của tour du lịch
                    int[] reversedSegment = Arrays.copyOfRange(bestRoute, i, j + 1);
                    for (int p = 0; p < reversedSegment.length; p++) {
                        bestRoute[i + p] = reversedSegment[reversedSegment.length - 1 - p];
                    }
                    bestRoute[bestRoute.length - 1] = bestRoute[0];

                    double newDistance = distanceCalc(distanceMatrix, bestRoute);

                    // Nếu tổng khoảng cách của tour du lịch sau khi hoán đổi nhỏ hơn tổng khoảng cách tour du lịch ban đầu
                    if (cityList[cityList.length - 1] > newDistance) {
                        // Thực hiện hoán đổi
                        System.arraycopy(bestRoute, 0, cityList, 0, bestRoute.length);
                    }
                    // Khôi phục tour du lịch về trạng thái trước khi hoán đổi
                    System.arraycopy(seed, 0, bestRoute, 0, seed.length);
                }
            }

            count++;

            // Tiếp tục xét số lần lặp
            if (distance > cityList[cityList.length - 1] && recursiveSeeding < 0) {
                distance = cityList[cityList.length - 1];
                count = -2;
                recursiveSeeding = -1;
            } else if (cityList[cityList.length - 1] >= distance && recursiveSeeding < 0) {
                count = -1;
                recursiveSeeding = -2;
            }
        }

        return cityList;
    }

    public static void main(String[] args) {
        // Example usage
        int[][] distanceMatrix = {
                {0, 1, 2, 3},
                {1, 0, 4, 5},
                {2, 4, 0, 6},
                {3, 5, 6, 0}
        };

        int[] cityTour = {1, 2, 3, 4, 1};

        int[] improvedTour = localSearch2Opt(distanceMatrix, cityTour, -1);

        // In tour du lịch được cải thiện
        System.out.println(Arrays.toString(improvedTour));
    }
}

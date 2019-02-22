public class KT14_2
{
    private static int partition(int[] a_list, int first, int last)
    {
        int pivot_value = a_list[first] ;
        int left_mark = first + 1 ;
        int right_mark = last ;

        boolean done = false ;
        while (!done)
        {

            while (left_mark <= right_mark && a_list[left_mark] < pivot_value)  left_mark ++ ;

            while (a_list[right_mark] >= pivot_value && right_mark >= left_mark)  right_mark -- ;

            if (right_mark < left_mark) done = true ;
            else
            {
                int temp = a_list[left_mark] ;
                a_list[left_mark] = a_list[right_mark] ;
                a_list[right_mark] = temp ;
            }
        }

        int temp = a_list[first] ;
        a_list[first] = a_list[right_mark] ;
        a_list[right_mark] = temp ;

        return right_mark ;
    }

    private static void quickSortHelper(int[] a_list, int first, int last)
    {
        if (first < last)
        {
            int split_point = partition(a_list, first, last) ;
            quickSortHelper(a_list, first, split_point - 1);
            quickSortHelper(a_list, split_point + 1 , last);
        }
    }

    private static void quickSort(int[] a_list)
    {
        int len = a_list.length ;
        quickSortHelper(a_list, 0, len - 1);
    }

    public static void main(String[] args)
    {
        int[] a_list = {54, 26, 93, 17, 77, 31, 44, 55, 20} ;
        quickSort(a_list) ;

        for (int x : a_list)
        {
            System.out.print(x);
            System.out.print(" ");
        }

    }
}
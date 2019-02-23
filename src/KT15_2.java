public class KT15_2
{
    private static void selectionSort(int[] a_list)
    {
        int len = a_list.length ;

        for (int fill_slot = len - 1; fill_slot > 0; fill_slot--)
        {
            int position_of_max = 0 ;

            for (int i = 1; i <= fill_slot; i++)
            {
                if (a_list[i] > a_list[position_of_max])
                {
                    position_of_max = i ;
                }
            }

            int temp = a_list[fill_slot] ;
            a_list[fill_slot] = a_list[position_of_max] ;
            a_list[position_of_max] = temp ;
        }
    }

    public static void main(String[] args)
    {
        int[] a_list = {54, 26, 93, 17, 77, 31, 44, 55, 20} ;
        selectionSort(a_list);

        for (int x:
                a_list) {
            System.out.print(x+" ");
        }
    }
}
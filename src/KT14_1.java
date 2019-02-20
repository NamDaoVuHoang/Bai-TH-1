public class KT14_1
{
    private static void insertionSort(int[] a_list)
    {
        int len = a_list.length ;
        for (int i = 0 ; i < len-1 ; i++)
        {
            int max_position = i;
            int position = i+1 ;

            while (position < len )
            {
                if (a_list[position] > a_list[max_position])
                max_position = position ;
                position ++ ;
            }

            int temp = a_list[i];
            a_list[i] = a_list[max_position] ;
            a_list[max_position] = temp ;
        }

    }

    public static void main (String[] args)
    {
        int[] a_list = {54 , 26 , 93 , 17 , 77 , 31 , 44 , 55 ,20} ;
        insertionSort(a_list);
        for(int  x : a_list )
        {
            System.out.print(x);
            System.out.print(" ");
        }
    }
}
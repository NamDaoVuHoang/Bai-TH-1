public class KT14_1
{
    private static void insertionSort(int[] a_list)
    {
        int len = a_list.length ;

        for (int index = 1 ; index < len ; index++)
        {
            int current_value = a_list[index] ;
            int position = index ;

            while (position > 0 && a_list[position - 1] > current_value)
            {
                a_list[position] = a_list[position - 1] ;
                position = position - 1 ;
            }

            a_list[position] = current_value ;
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

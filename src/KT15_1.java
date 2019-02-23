public class KT15_1
{
    public static void bubbleSort(int[] a_list)
    {
        int len = a_list.length ;

        for (int pass_num = len - 1; pass_num > 0; pass_num--)
        {
            for (int i = 0; i < pass_num; i++)
            {
                if (a_list[i] > a_list[i+1])
                {
                    int temp = a_list[i] ;
                    a_list[i] = a_list[i+1] ;
                    a_list[i+1] = temp ;
                }
            }
        }
    }

    public static void main(String[] args)
    {
        int[] a_list = {54, 26, 93, 17, 77, 31, 44, 55, 20} ;
        bubbleSort(a_list);

        for (int x:
             a_list) {
            System.out.print(x+" ");
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;

namespace DynamicFibonacciSequence
{
    using System;

    class GFG
    {
        static int MAX = 100000000;
        static BigInteger[] f;
        public static BigInteger fib(int n)
        {


            if (n == 0)
                return 0;

            if (n == 1 || n == 2)
                return (f[n] = 1);

            if (f[n] != 0)
                return f[n];


            int k = (n & 1) == 1 ? (n + 1) / 2
                                 : n / 2;

            f[n] = (n & 1) == 1 ? (fib(k) * fib(k) +
                                   fib(k - 1) * fib(k - 1))
                                : (2 * fib(k - 1) + fib(k)) *
                                                    fib(k);

            return f[n];
        }

        static void Main()
        {
            string programRun = "Y";

            while (programRun == "Y")
            {
                Console.Clear();
                Console.WriteLine("Pick a factor in the Fibonacci Sequence between 1 & 99999999");
                string fibonnaci = "f";
                int n1;
                do
                {

                    fibonnaci = Console.ReadLine();
                    n1 = int.Parse(fibonnaci);

                    if (n1 >= 100000000)
                    {
                        Console.WriteLine("That integer is higher than 99999999! Please try again.");
                    }
                } while (n1 >= 100000000);
                int n = n1;

                f = new BigInteger[MAX];
                Console.WriteLine("\nThe answer is: " + fib(n));

                Console.WriteLine("\nWould you like to run the program again? [Y/N]");
                programRun = Console.ReadLine();
            }
            Console.WriteLine("Press any key to continue!");
            Console.ReadKey();

        }
    }
}
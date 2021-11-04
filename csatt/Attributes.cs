using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Öznitelikler
{
    class Program
    {
        static void Main(string[] args)
        {

            Student student = new Student { Std_Id = 01, Std_FirstName = "Alican", Std_LastName = "AKCA", Std_Number = 2020 };
            Student_Affairs Student_Affairs = new Student_Affairs();
            Student_Affairs.Reg(student);
            Console.ReadLine();
        }
        [AttributeUsage(AttributeTargets.All, AllowMultiple = true)]
        class AttExAttribute : Attribute
        {
            public string _ExString;
            public AttExAttribute(string ExString)
            {
                _ExString = ExString;
            }
        }

        [AttEx("Student")]
        [AttEx("AllStudents")]
        class Student
        {
            public int Std_Id { get; set; }
            public string Std_FirstName { get; set; }
            public string Std_LastName { get; set; }
            public int Std_Number { get; set; }
        }
        class Student_Affairs
        {
            [Obsolete("Ana metot Reg'dir. Lütfen NewReg metodunu kullan.")]
            public void Reg(Student student)
            {

                Console.WriteLine("{0},{1},{2},{3} student registration is successful!",
                    student.Std_Id, student.Std_FirstName, student.Std_LastName, student.Std_Number);
            }

            public void NewReg(Student student)
            {
                Console.WriteLine("{0},{1},{2},{3} student registration is successful!",
                    student.Std_Id, student.Std_FirstName, student.Std_LastName, student.Std_Number);
            }
        }

    }
}

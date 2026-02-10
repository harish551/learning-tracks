// use std::fmt;

fn main() {
    // scalar data types
    let num: u32 = 1234;
    let dec: f32 = 123.4;
    let b_value = true;
    let c_value = false;
    let character: char = 'X';
    
    println!("{} {} {} {} {}", num, dec, b_value, c_value, character);

    let a = 10;
    let b = 2;
    let c = 3.5;
    let d = 1.5;

    // addition
    let sum = a + b;
 
    // substraction
    let sub = a - b;
    let dec_sub = c - d; 
   
    // product
    let prod = a * b;

    // devision
    let div = a / b;

    // reminder
    let rem = a % b;

    println!("{} {} {} {} {} {}", sum, sub, dec_sub, prod, div, rem);

    // let c = 2.5;
    // let dec_sum: f32 = a + c;
    // println!("{}", dec_sum);

    // compound data types

    // tuples 
    let tup: (i32, f64, u64, char, bool) = (-123, 1234.5, 1234567, 'C', true);
    println!("first item in the tuple is {}", tup.0);
    println!("second item in the tuple is {}", tup.1);
    println!("forth item in the tuple is  {}", tup.3);

    // arrays
    let arr = [1, 2, 3, 4, 5];
    let arr2 = ['a', 'b', 'c', 'd', 'e'];
    let arr3 = ["one", "two", "three", "four"];
    let arr4 = [10; 5];
    let arr5: [i32; 5] = [-1, -2, 0, 1, 2];

    // println!("array examples:");
    println!("first element of arr: {}", arr[0]);
    println!("second element of the arr2: {}", arr2[1]);
    println!("third element of the arr3: {}", arr3[2]);
    println!("fifth element of the arr5: {}", arr5[1]);

    // fmt::Display("{}", arr);

}

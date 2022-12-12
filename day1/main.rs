use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(Debug)]
struct Elf {
    foods: Vec<i32>
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn total_calories(elf: &Elf)-> i32
{
    let mut n: i32 = 0;
    for food in elf.foods.iter()
    {
        n += food;
    }
    n
}

fn get_food_from_file(file_path: &str) -> Vec<Elf>
{
    let mut foods: Vec<i32> = vec![];
    let mut list: Vec<Elf> = vec![];
    if let Ok(lines) = read_lines(file_path) {
        for line in lines {
            if let Ok(food) = line {
                match food.parse::<i32>() {
                    Ok(v) => foods.push(v),
                    Err(_) => {
                        list.push(Elf { foods : foods.clone() });
                        foods.clear();
                    }
                }
            }
        }
    }
    list
}

fn main()
{
    let elves = get_food_from_file("./filename");
    let mut total_calories_per_elf = vec![];

    for elf in elves
    {
        total_calories_per_elf.push(total_calories(&elf));
    }

    total_calories_per_elf.sort();
    total_calories_per_elf.reverse();

    let max = total_calories_per_elf.iter().max();
    let mut combined_three_max_values: i32 = 0;

    for i in 0..3
    {
        combined_three_max_values += total_calories_per_elf[i];
    }

    println!("combined top three values: {:?}", combined_three_max_values );
    println!("max value: {:?}", max.unwrap());
}

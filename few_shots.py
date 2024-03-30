few_shots = [
    {
        "Question": "How many products with a stock quantity less than 5?",
        "SQLQuery": "SELECT COUNT(*) FROM pc_factory.pc_inventory where stock_quantity < 5;",
        "Answer": "4",
    },
    {
        "Question": "how many gaming pc model x is there",
        "SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory where name = 'Gaming PC - Model X';",
        "Answer": "10",
    },
    {
        "Question": "How many Gaming PC - Model X are there",
        "SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory  where name= 'Gaming PC - Model X';",
        "Answer": "10",
    },
    {   "Question": "what is the total worth of gaming pc available in stock",
        "SQLQuery": "SELECT stock_quantity*price FROM pc_factory.pc_inventory  where name= 'Gaming PC - Model X';",
        "Answer": "15000.00",
    },
    {.
"Question": "How many products with a stock quantity less than 5?",
"SQLQuery": "SELECT COUNT(*) FROM pc_factory.pc_inventory WHERE stock_quantity < 5;",
"Answer": "4"
},
{
"Question": "How many Gaming PC - Model X are there?",
"SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory WHERE name = 'Gaming PC - Model X';",
"Answer": "10"
},
{
"Question": "What is the total worth of Gaming PC - Model X?",
"SQLQuery": "SELECT stock_quantity * price FROM pc_factory.pc_inventory WHERE name = 'Gaming PC - Model X';",
"Answer": "15000.00"
},
{
"Question": "How many Professional Workstation - Model Y are in stock?",
"SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory WHERE name = 'Professional Workstation - Model Y';",
"Answer": "8"
},
{
"Question": "What is the total value of all Ultra-Portable Laptops - Model C?",
"SQLQuery": "SELECT stock_quantity * price FROM pc_factory.pc_inventory WHERE name = 'Ultra-Portable Laptop - Model C';",
"Answer": "14400.00"
},
{
"Question": "How many Chromebooks - Model G are available?",
"SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory WHERE name = 'Chromebook - Model G';",
"Answer": "25"
},
{
"Question": "What is the discount percentage for Student Laptop - Model B?",
"SQLQuery": "SELECT pct_discount FROM pc_factory.discounts JOIN pc_factory.pc_inventory ON pc_factory.discounts.product_id = pc_factory.pc_inventory.product_id WHERE pc_factory.pc_inventory.name = 'Student Laptop - Model B';",
"Answer": "NULL"
},
{
"Question": "How many 2-in-1 Convertible Laptops - Model E are in stock?",
"SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory WHERE name = '2-in-1 Convertible Laptop - Model E';",
"Answer": "10"
},
{
"Question": "What is the total worth of Media Editing PC - Model A?",
"SQLQuery": "SELECT stock_quantity * price FROM pc_factory.pc_inventory WHERE name = 'Media Editing PC - Model A';",
"Answer": "12500.00"
},
{
"Question": "How many Business Laptops - Model F are available?",
"SQLQuery": "SELECT stock_quantity FROM pc_factory.pc_inventory WHERE name = 'Business Laptop - Model F';",
"Answer": "8"
}
] 
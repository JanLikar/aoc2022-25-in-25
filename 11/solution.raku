my @primes = (2, 3, 5, 7, 11, 13, 17, 19);
my $PRIMES_PRODUCT = [*] @primes;


grammar Monkeys {
    rule  TOP  { (<monkey>)* }

    rule monkey {
        <header>
        <items>
        <operation>
        <test>
        <if_true>
        <if_false>
    }

    token header { "Monkey "\d":" }

    rule items { "Starting items:" (<number>+ ','? )+ }

    rule operation { "Operation: new = old" <operator> <operand> }
    token operator { "+" | "*" }
    token operand { <number> | "old"}

    rule test { "Test: divisible by" <number> }
    rule if_true { "If true: throw to monkey" <number> }
    rule if_false { "If false: throw to monkey" <number> }

    token number { \d+ }
};


multi sub evaluate_operation("+", $a, $b) { $a + $b }
multi sub evaluate_operation("*", $a, $b) { $a * $b }


sub load_monkeys(@monkeys, @items, @inspection_counts) {
    my $contents = slurp "input.txt";
    my $raw_monkeys = Monkeys.parse($contents);

    for $raw_monkeys[0] -> $monkey {
        my $m = $monkey<monkey>;

        my @parsed_items;

        for $m<items>[0] -> $item {
            push(@parsed_items, $item<number>[0].Int)
        }
        push(@items, @parsed_items);
        @inspection_counts.push(0);
 
        my %parsed_monkey =  (
            if_true => $m<if_true><number>.Int,
            if_false => $m<if_false><number>.Int,
            test => $m<test><number>.Int,
            operator => $m<operation><operator>.Str,
            operand => $m<operation><operand>.Str,
        );
        push(@monkeys, %parsed_monkey);
    }
}


sub monkey_business($rounds = 20, $divide_by_3 = True) {
    my @monkeys;
    my @items;
    my @inspection_counts;

    load_monkeys(@monkeys, @items, @inspection_counts);

    for ^$rounds -> $round {
        for @monkeys.kv -> $i, $monkey {
            for @items[$i].keys -> $j {
                @inspection_counts[$i] += 1;

                my $item = @items[$i][$j];
                my $operand;

                if $monkey<operand> eq "old" {
                    $operand = $item;
                }
                else {
                    $operand = $monkey<operand>.Int;
                }

                $item = evaluate_operation($monkey<operator>, $operand, $item);

                if $divide_by_3 {
                    $item = $item div 3;
                }

                $item = $item % $PRIMES_PRODUCT;
                
                if $item %% $monkey<test> {
                    @items[$monkey<if_true>].push($item);
                }
                else {
                    @items[$monkey<if_false>].push($item);
                }

            }
            @items[$i] = []
        }
    }

    say [*] @inspection_counts.sort.tail(2);
}

monkey_business;
monkey_business(10000, False);

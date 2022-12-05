<?php

function print_stack_top($stacks) {
    foreach ($stacks as $stack) {
        print($stack[count($stack) - 1]);
    }
    print("\n");
}

function load_stacks() {
    $input_stacks = file_get_contents("input_stacks.txt");
    $input_stacks_lines = array_reverse(explode("\n", $input_stacks));
    
    $num_stacks = count(preg_split('/\s+/', trim($input_stacks_lines[0])));
    
    $stacks = array_fill(0, $num_stacks, array());
    
    foreach (array_slice($input_stacks_lines, 1) as $line) {
        for ($i = 0; $i < strlen($line); $i++) {
            if ($line[$i] == " " || $line[$i] == "[" || $line[$i] == "]") {
                continue;
            }
            array_push($stacks[intdiv($i - 1, 4)], $line[$i]);
        }
    }

    return $stacks;
}

$part_1_stacks = load_stacks();
$part_2_stacks = load_stacks();

$instructions = file_get_contents("input.txt");

$matches = array();
preg_match_all('/move ([0-9]+) from ([0-9]+) to ([0-9]+)/', $instructions, $matches);

for ($i = 0; $i < count($matches[0]); $i++) {
    $packets_to_move = (int)$matches[1][$i];
    $from_stack = (int)$matches[2][$i];
    $to_stack = (int)$matches[3][$i];

    // Part 1
    for ($j = 0; $j < $packets_to_move; $j++) {
        $popped = array_pop($part_1_stacks[$from_stack - 1]);
        
        array_push($part_1_stacks[$to_stack - 1], $popped);
    }

    // Part 2
    $popped = array_splice($part_2_stacks[$from_stack - 1], -$packets_to_move, $packets_to_move);
    $part_2_stacks[$to_stack - 1] = array_merge($part_2_stacks[$to_stack - 1], $popped);
}

print_stack_top($part_1_stacks);
print_stack_top($part_2_stacks);

?>

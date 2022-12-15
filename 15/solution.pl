use strict; use warnings;

sub distance {
    my ($ax, $ay, $bx, $by) = @_;
    return abs($ax - $bx) + abs($ay - $by);
}

open my $handle, '<', 'input.txt';
chomp(my @lines = <$handle>);

my @beacon_xs = ();
my @beacon_ys = ();
my %beacons_set;

my @sensor_xs = ();
my @sensor_ys = ();

my @ranges = ();


foreach my $line (@lines) {
    if($line =~ /^Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)$/) {
        my ($sensor_x, $sensor_y, $beacon_x, $beacon_y) = ($1, $2, $3, $4);

        my @beacon = ($beacon_x, $beacon_y);
        my @sensor = ($sensor_x, $sensor_y);

        push(@beacon_xs, $beacon_x);
        push(@beacon_ys, $beacon_y);
        push(@sensor_xs, $sensor_x);
        push(@sensor_ys, $sensor_y);

        my $range = distance($beacon_x, $beacon_y, $sensor_x, $sensor_y);
        push(@ranges, $range);

        $beacons_set{"$beacon_x,$beacon_y"} = ();
    }
}

my $output_line = 2000000;
my %covered_squares;

# Part 1.
for (my $i = 0; $i < @beacon_xs; $i++) {
    my $range = $ranges[$i];

    for(my $j = 0; $j < $range; $j++) {
        my $left_x = $sensor_xs[$i] - $j;
        my $right_x = $sensor_xs[$i] + $j;

        if(distance($left_x, $output_line, $sensor_xs[$i], $sensor_ys[$i]) <= $range) {
            if(!exists($beacons_set{"$left_x,$output_line"})) {
                $covered_squares{$left_x} = 1;
            }
            if(!exists($beacons_set{"$right_x,$output_line"})) {
                $covered_squares{$right_x} = 1;
            }     
        } else {
            last;
        }
    }
}

print %covered_squares . "\n";


# Part 2.

sub all_sensors_out_of_range {
    my $x = $_[0];
    my $y = $_[1];

    for (my $i = 0; $i < @sensor_xs ; $i++) {
        my $sensor_range = $ranges[$i];
        my $dist = distance($x, $y, $sensor_xs[$i], $sensor_ys[$i]);

        if($dist <= $sensor_range ) {
            return 0;
        }
    }

    return 1;
}

for (my $i = 0; $i < @sensor_xs ; $i++) {
    my $range = $ranges[$i];
    my @dvec = ([1, 1], [1, -1], [-1, -1], [-1, 1]);

    my $current_x = $sensor_xs[$i] - $range - 1;
    my $current_y = $sensor_ys[$i];

    for(my $vec_idx = 0; $vec_idx < 4; $vec_idx++) {
        for(my $j = 0; $j <= $range; $j++) {
            $current_x += $dvec[$vec_idx][0];
            $current_y += $dvec[$vec_idx][1];

            if(0 < $current_x && $current_x < 4000000 && 0 < $current_y && $current_y < 4000000) {
                if(all_sensors_out_of_range($current_x, $current_y)) {
                    print $current_x * 4000000 + $current_y . "\n";
                    exit();
                }
            }
        }
    }
}

close $handle;

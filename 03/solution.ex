defmodule Solution do
  def line_priority(input_line) do
    pivot = trunc(length(input_line) / 2)

    Enum.chunk_every(input_line, pivot)
      |> list_dupes
      |> Enum.map(&item_priority/1)
      |> Enum.sum
  end

  def list_dupes(lst) do
    lst
      |> Enum.map(&MapSet.new/1)
      |> Enum.reduce(&MapSet.intersection/2)
  end

  def priority_of_tripplets(tripplet) do
      tripplet
        |> Enum.map(&:binary.bin_to_list/1)
        |> list_dupes
        |> Enum.map(&item_priority/1)
        |> Enum.sum
  end

  def item_priority(item) do
    # az and AZ map to 1 through 26 and 27 through 52.
    if 64 < item and item < 91 do
      # Uppercase
      item - 38
    else
      # Lowercase
      item - 96
    end
  end
end

File.stream!("input.txt")
  |> Stream.map(&String.trim/1)
  |> Stream.map(&:binary.bin_to_list/1)
  |> Stream.map(&Solution.line_priority/1)
  |> Enum.sum
  |> IO.puts

File.stream!("input.txt")
  |> Stream.map(&String.trim/1)
  |> Stream.chunk_every(3)
  |> Stream.map(&Solution.priority_of_tripplets/1)
  |> Enum.sum
  |> IO.puts

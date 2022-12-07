const fs = require('fs');

const input_lines = fs.readFileSync('input.txt', 'utf8').split(/\r?\n/)

const ROOT = "/"
let total_filesize = 0
let folder_sizes = {}
let pwd = [ROOT]

for (let line of input_lines) {
    const parts = line.split(" ")
    const isCommand = parts[0] == "$"
    const isCd = isCommand && parts[1] == "cd"

    if(isCd && parts[2] == "..") {
        pwd.pop()
    }
    else if (isCd && parts[2] != "/") {
        pwd.push(parts[2])
    }
    else if (!isCommand && parts[0] != "dir") {
        size = parseInt(parts[0])
        
        let tmp = [...pwd]
        
        while(tmp.length > 0) {
            key = tmp.join(".")

            if(!(key in folder_sizes)) {
                folder_sizes[key] = 0
            }

            folder_sizes[key] += size
            tmp.pop()
        }
        
        total_filesize += size
    }
}

const smaller_than = Object.values(folder_sizes).filter(n => n <= 100_000)

console.log(smaller_than.reduce((acc, elem) => acc + elem, 0))

const usage = folder_sizes[ROOT]
const total_size = 70000000
const required_size = 30000000
const min_size_to_delete = required_size + usage - total_size

const deletion_candidates = Object.values(folder_sizes).filter(n => n >= min_size_to_delete)
console.log(Math.min(...deletion_candidates))

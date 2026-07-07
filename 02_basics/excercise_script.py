def process_file(input_file, output_file):
    try:
        f = open(input_file, "r")
        f_out = open(output_file, "w")
        for line in f:
            f_out.write(line)

        f.close()
        f_out.close()
    except Exception as e:
        print("Something went wront ", e)


process_file("funny.txt", "test2.txt")

Task 1


1.ls

I see(output):
anaconda2  Downloads  Public   Templates
Desktop    Music      Scripts  Umuzi
Documents  Pictures   Stini    Videos

This means:
these are all the directories in my root directory."ls-lists all the contents of a specified directory"(j.lee 2012)

2.pwd

i see:
/home/kevin

This means:
this is my current working directory. pwd stand for ,print working directory.

3.mkdir workspace
cd workspace


4.ls

I see: 
nothing

This means:
it returns nothing becuase there isn't anything in the directory yet.

5.touch README.md

6.cp README.md CHANGELOG.md

Task 2

 touch exercise.md
mv exercise.md ../../tmp
rm exercise.md /tmp 
 

Task 3
1. touch umuzi.md recruits.md cohort.md
2. echo " I know why you're here, Neo. I know what you've been doing... why you hardly sleep, why you live alone, and why night after night, you sit by your computer. You're looking for him. I know because I was once looking for the same thing. And when he found me, he told me I wasn't really looking for him. I was looking for an answer. It's the question that drives us, Neo. It's the question that brought you here. You know the question, just as I did" >cohort.md
echo "Well, I mean, yes idealism, yes the dignity of pure research, yes the pursuit of truth in all its forms, but there comes a point I'm afraid where you begin to suspect that the entire multidimensional infinity of the Universe is almost certainly being run by a bunch of maniacs. And if it comes to a choice between spending yet another ten million years finding that out, and on the other hand just taking the money and running, then I for one could do with the exercise." >recruits.md
 echo "Nobody exists on purpose. Nobody belongs anywhere. We’re all going to die. Come watch TV." >umuzi.md

3. cat umuzi.md cohort.md recruits.md

4. cat umuzi.md cohort.md recruits.md >summary.md

5. echo " The End" >>summary.md

Task 4

1. locate  umuzi

2. locate umuzi >search_result.md

Task 5

1. touch pad.md /home/kevin/Documents

2. cd ../Desktop
mkdir work

3. cp /home/kevin/Documents/pad.md ./pad_copy.md 

4. locate updatedb
sudo updatedb

5. cd -

6. locate pad_copy.md

Task 6

1. find / -name '*pdf'

2.find / -name  '*pdf' >/home/kevin/Documents/choice.md

3. find / -mtime -1

Task 7 

1. nano my_bio.md

2. ctrlx

3. mkdir my_files
mv my_bio.md my_files

Task 8

1. sudo apt update

2. sudo apt upgrade

4. sudo apt install tree

5. sudo dpkg -i code_1.43.1-1584515895_amd64.deb

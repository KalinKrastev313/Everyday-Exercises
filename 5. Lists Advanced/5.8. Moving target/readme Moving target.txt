The script is one possible solution of the following exercise: 

8. * Moving Target
You are at the shooting gallery again and you need a program that helps you keep track of moving targets. On the
first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start
receiving commands for manipulating the targets, until the "End" command. The commands are the following:
 Shoot {index} {power}
o Shoot the target at the index, if it exists by reducing its value by the given power (integer value).A
target is considered shot when its value reaches 0.
o Remove the target, if it is shot.
 Add {index} {value}
o Insert a target with the received value at the received index, if it exist. If not, print: "Invalid
placement";
 Strike {index} {radius}
o Remove the target at the given index and the ones before and after it depending on the radius, if
such exist. If any of the indices in the range is invalid print:
"Strike missed!" and skip this command.
Example: Strike 2 2
{radius
}

{radius
}

{strikeIndex
}

{radius
}

{radius
}

 End
o Print the sequence with targets in the following format:
{target 1 }|{target 2 }…|{target n }

Input / Constraints
 On the first line you will receive the sequence of targets – integer values [1-10000].
 On the next lines, until the "End" will be receiving the command described above – strings.
 There will never be a case when "Strike" command would empty the whole sequence.
Output
 Print the appropriate message in case of "Strike" command if necessary.
 In the end, print the sequence of targets in the format described above.

Examples

Input 				Output 				Comments
52 74 23 44 96 110		Invalid placement!		The first command is &quot;Shoot&quot;, so we
Shoot 5 10			52|100				reduce the target on index 5, which
Shoot 1 80							is valid, with the given power – 10.
Strike 2 1							Then we receive the same command but
Add 22 3							we need to reduce the target on the
End								1 st index, with power 80. The value of
								this target is 74, so it is
								considered shot and we remove it.
								Then we receive the &quot;Strike&quot; command
								on the 2 nd index and we need to check












#!/bin/bash
#
# createmodule.sh - Takes the name of a environment init script and 
# produces a modulefile that duplicates the changes made by the init script
#
# Copyright (C) 2010 by Orion E. Poplawski
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

if [ -z "$1" ]
then
  echo "usage: $0 <initscript> [args]" 1>&2
  exit 1
fi

#Will print out array assignment list
printenvarray () {
  env | while read x
  do
    key=${x%%=*}
    value=${x#*=}
    echo [$key]="'$value'"
  done
}

#Apparently we need to declare the associative arrays
declare -A env1 env2

#Record starting environment
eval env1=(`printenvarray`)

#Source the environment script
. "$@"

#Record ending environment
eval env2=(`printenvarray`)

#Print out the modulefile
echo "#%Module 1.0"

#Keys that changed
for key in "${!env1[@]}"
do
   if [ "${env1[$key]}" != "${env2[$key]}" ]
   then
      #Working directory change
      if [ "$key" = PWD ]
      then
	echo -e "chdir\t\t${env2[PWD]}"
      #Test for delete
      elif [ -z "${env2[$key]}" ]
      then
         echo -e "unsetenv\t${key}\t${env2[$key]}"
      #Test for prepend
      elif [ "${env2[$key]%${env1[$key]}}" != "${env2[$key]}" ]
      then
         added="${env2[$key]%${env1[$key]}}"
         echo -e "prepend-path\t$key\t${added%:}"
      #Test for append
      elif [ "${env2[$key]#${env1[$key]}}" != "${env2[$key]}" ]
      then
         added="${env2[$key]#${env1[$key]}}"
         echo -e "append-path\t$key\t${added#:}"
      else
         #Unhandled
         echo "Unhandled change of $key" 1>&2
         echo "Before <${env1[$key]}>" 1>&2
         echo "After  <${env2[$key]}>" 1>&2
      fi
   fi
   #Delete keys we've handled
   unset env1[$key]
   unset env2[$key]
done

#New keys
for key in "${!env2[@]}"
do
   if [ "$key" = OLDPWD ]
   then
      continue
   fi
   #Use prepend-path for new paths
   if [ "${key/PATH/}" != "$key" ]
   then
     echo -e "prepend-path\t${key}\t${env2[$key]}"
   else
     echo -e "setenv\t\t${key}\t${env2[$key]}"
   fi
done

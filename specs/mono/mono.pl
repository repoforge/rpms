#!/usr/bin/perl

while(<>) {
	$line=$_;
	if ($line=~m| target="([^"]+)"|) {
		$lib=$1;
		if (($new=readlink("/lib/$lib")) or ($new=readlink("/usr/lib/$lib"))) {
			$line=~s| target="$lib"| target="$new"|;
		}
	}
	print $line;
}

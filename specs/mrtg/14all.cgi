#!/usr/bin/perl -w
#
# 14all.cgi
#
# create html pages and graphics with rrdtool for mrtg + rrdtool
#
# (c) 1999 Rainer.Bawidamann@informatik.uni-ulm.de
#
# use freely, but: NO WARRANTY - USE AT YOUR OWN RISK!
#
# 1999-08-19
#	* v0.1
#	* first release
# 1999-08-25
#	* v0.2
#	* recognizes more options: perhour, perminute, integer
#	* integrates fully in mrtg (-> 2.8.7) with "useRRDTool: Yes"-switch
# 1999-08-27
#	* v0.3
#	* more options: bits
#	* mrtg/rrd-patch runs without installed rrdtools perl module
#

my $version = "14all.cgi v0.3";

use strict;
use CGI;

sub print_error(@);
sub read_mrtg_config();

my ($q, %targets, @sorted, %config, $cfgfile);
my ($cgidir);

### where the mrtg.cfg file is
#$cfgfile = '/home/mrtg/mrtg.cfg';
$cfgfile = '/home/rb1/public_html/mrtg/mrtg.cfg';
###

# initialize CGI
$q = new CGI;
$q->import_names('CGI');
my $meurl = $q->url();
$meurl =~ m|^[^/]+//([^/]+)(/[^/]+)*(/[^/])$|;

# read the config file
read_mrtg_config();

# the footer we print on every page
my $footer = <<"EOT";
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR>
    <TD WIDTH=63><A ALT="MRTG"
    HREF="http://ee-staff.ethz.ch/~oetiker/webtools/mrtg/mrtg.html"><IMG
    BORDER=0 SRC="$config{icondir}mrtg-l.gif"></A></TD>
    <TD WIDTH=25><A ALT=""
    HREF="http://ee-staff.ethz.ch/~oetiker/webtools/mrtg/mrtg.html"><IMG
    BORDER=0 SRC="$config{icondir}mrtg-m.gif"></A></TD>
    <TD WIDTH=388><A ALT=""
    HREF="http://ee-staff.ethz.ch/~oetiker/webtools/mrtg/mrtg.html"><IMG
    BORDER=0 SRC="$config{icondir}mrtg-r.gif"></A></TD>
  </TR>
</TABLE>
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0>
  <TR VALIGN=top>
  <TD WIDTH=88 ALIGN=RIGHT><FONT FACE="Arial,Helvetica" SIZE=2>Version 2.8.6-rrd</FONT></TD>
  <TD WIDTH=388 ALIGN=RIGHT><FONT FACE="Arial,Helvetica" SIZE=2>
  <A HREF="http://ee-staff.ethz.ch/~oetiker/">Tobias Oetiker</A>
  <A HREF="mailto:oetiker\@ee.ethz.ch">&lt;oetiker\@ee.ethz.ch&gt;</A> and
  <A HREF="http://www.bungi.com">Dave&nbsp;Rand</A>&nbsp;
  <A HREF="mailto:dlr\@bungi.com">&lt;dlr\@bungi.com&gt;</A>
  <TR VALIGN=top>
  <TD WIDTH=88 ALIGN=RIGHT><FONT FACE="Arial,Helvetica" SIZE=2>$version</FONT></TD>
  <TD WIDTH=388 ALIGN=RIGHT><FONT FACE="Arial,Helvetica" SIZE=2>
  <A HREF="http://www.uni-ulm.de/~rbawidam/">Rainer&nbsp;Bawidamann</A>&nbsp;
  <A HREF="mailto:rb1\@informatik.uni-ulm.de">&lt;rb1\@informatik.uni-ulm.de&gt;</A></FONT>
  </TD>
</TR>
</TABLE>
EOT
$footer .= $q->end_html;

# the main switch
if (!$q->param) {
	# no parameter - show a list of directories and targets without "Directory[...]" (aka root-targets)
	print $q->header, $q->start_html(
	-title => "MRTG/RRD $version",
	-author => 'Rainer.Bawidamann@informatik.uni-ulm.de',
	-bgcolor => $config{background},
	-expires => '+1h'); # this page changes whenever directories are added/deleted in mrtg.cfg
	my (@dirs, %dirs, @logs);
	# get the list of directories and "root"-targets
	foreach my $tar (@sorted) {
		next if $tar eq '_'; # _ is default settings, not a real target
#		if (exists $targets{$tar}{directory} && ($targets{$tar}{directory} ne '.')) {
		if ($targets{$tar}{directory}) {
			next if exists $dirs{$targets{$tar}{directory}};
			$dirs{$targets{$tar}{directory}} = $tar;
			push @dirs, $targets{$tar}{directory};
		} else {
			push @logs, $tar;
		}
	}
	print $q->h1("Available Targets"),"\n";
	if ($#dirs > -1) {
		print $q->h2("Directories"),"\<ul>\n";
		foreach my $tar (@dirs) {
			print $q->li($q->a({href => "$meurl?dir=$tar"},
				"Group $tar")),"\n";
		}
		print '</ul><hr>';
	}
	if ($#logs > -1) {
		print $q->h2("Targets"),"\n\<table>\n";
		foreach my $tar (@logs) {
			next if $tar eq '_';
			next if $targets{$tar}{directory} ne $CGI::dir;
			print '<tr><td>',$q->a({href => "$meurl?log=$tar"},
				"$targets{$tar}{title}"),'<td>',
				$q->img({src => "$meurl?log=$tar&png=daily&small=1", alt => "daily-graph"}),
				"\n";
		}
		print '</table>';
	}
	print $footer;
} elsif (defined $CGI::dir) {
	# show a list of targets in the given directory
	print $q->header, $q->start_html(
		-title => "MRTG/RRD - Group $CGI::dir",
		-author => 'Rainer.Bawidamann@informatik.uni-ulm.de',
		-bgcolor => $config{background},
		-expires => '+10m');
	print $q->h1("Available Targets"),"\n\<table>\n";
	foreach my $tar (@sorted) {
		next if $tar eq '_'; # _ is not a real target
		next if $targets{$tar}{directory} ne $CGI::dir;
		print '<tr><td>',$q->a({href => "$meurl?log=$tar"},
			"$targets{$tar}{title}"),'<td>',
			$q->a({href => "$meurl?log=$tar"},
			$q->img({src => "$meurl?log=$tar&png=daily&small=1", alt => "daily-graph"})),
			"\n";
	}
	print '</table>', $footer;
} elsif (defined $CGI::png) {
	# send a graphic, create it if necessary
	print_error("CGI call error") if (!defined $CGI::log);	
	my $workdir = "$config{workdir}/$targets{$CGI::log}{directory}/";
	my $rrd = "$workdir$CGI::log.rrd";
	my $pngfile = "$workdir$CGI::log-$CGI::png.png";
	if (!-w $workdir) {
		$pngfile = "/tmp/$CGI::log-$CGI::png.png";
	}
	$pngfile .= '-s' if (defined $CGI::small);
	my %expire = qw/daily +300s weekly +1800s monthly +2h yearly +1d/;
	my %start = qw/daily -86400 weekly -604800 monthly -2593000 yearly -31536000/;
	require 'RRDs.pm'; # load RRDs.pm only when needed
	# build the rrd command line: set the starttime and the graphics format (PNG)
	my @args = ($pngfile, '-s', $start{$CGI::png}, '-a', 'PNG');
	# if it's not a small picture set the legends
	my ($l1,$l2,$l3,$l4,$li,$lo) = ('','','','','','');
	if (!defined $CGI::small) {
		if ($targets{$CGI::log}{ylegend}) {
			push @args, '-v', $targets{$CGI::log}{ylegend}; }
		if ($targets{$CGI::log}{xsize}) {
			push @args, '-w', $targets{$CGI::log}{xsize}; }
		if ($targets{$CGI::log}{ysize}) {
			push @args, '-h', $targets{$CGI::log}{ysize}; }
		if ($targets{$CGI::log}{legend1}) {
			$l1 = ":".$targets{$CGI::log}{legend1}; }
		if ($targets{$CGI::log}{legend2}) {
			$l2 = ":".$targets{$CGI::log}{legend2}."\\l"; }
		if ($targets{$CGI::log}{legend3}) {
			$l3 = ":".$targets{$CGI::log}{legend3}; }
		if ($targets{$CGI::log}{legend4}) {
			$l4 = ":".$targets{$CGI::log}{legend4}."\\l"; }
		if ($targets{$CGI::log}{legendi}) {
			$li = $targets{$CGI::log}{legendi}; }
		else {	$li = "In:"; }
		$li =~ s':'\\:'; # ' quote :
		if ($targets{$CGI::log}{legendo}) {
			$lo = $targets{$CGI::log}{legendo}; }
		else {	$lo = "Out:"; }
		$lo =~ s':'\\:'; # ' quote :
		if ($targets{$CGI::log}{options}{integer}) {
			$li = $li . ' %.0lf';
			$lo = $lo . ' %.0lf';
		} else {
			$li = $li . ' %.3lf';
			$lo = $lo . ' %.3lf';
		}
		if ($targets{$CGI::log}{kmg}) {
			$li = $li . ' %s';
			$lo = $lo . ' %s';
		}
	} else {
		push @args, '-w',250,'-h',100;
	}
	push @args,'--alt-y-grid','--lazy','-c','MGRID#cc0000';
	my $factor = 1; # should we scale the values?
	if ($targets{$CGI::log}{options}{perminute}) {
		$factor = 60; # perminute -> 60x
	} elsif ($targets{$CGI::log}{options}{perhour}) {
		$factor = 3600; # perhour -> 3600x
	}
	if ($targets{$CGI::log}{options}{bits}) {
		$factor *= 8; # bits instead of bytes -> 8x
	}
	if ($factor > 1) {
		# scale the values. we need a CDEF for this
		push @args, "DEF:in0=$rrd:ds0:AVERAGE", "DEF:out0=$rrd:ds1:AVERAGE",
			"CDEF:in=in0,$factor,*","CDEF:out=out0,$factor,*";
	} else {
		push @args, "DEF:in=$rrd:ds0:AVERAGE", "DEF:out=$rrd:ds1:AVERAGE";
	}
	# the commands to draw the values
	push @args, "AREA:in#00cc00$l1", "LINE1:out#0000ff$l2";
	# the commands for the peaks
	push (@args,"DEF:min=$rrd:ds0:MAX", "DEF:mout=$rrd:ds1:MAX",
		"LINE1:min#006600$l3", "LINE1:mout#ff00ff$l4")
		if (!defined $CGI::small && (substr($CGI::png,0,1) =~ /[$targets{$CGI::log}{withpeak} ]/));
	# print the legends
	push @args, "GPRINT:out:MAX:Max $lo",
		"GPRINT:out:AVERAGE:Average $lo",
		"GPRINT:out:LAST:Current $lo\\l",
		"GPRINT:in:MAX:Max $li",
		"GPRINT:in:AVERAGE:Average $li",
		"GPRINT:in:LAST:Current $li\\l" if (!defined $CGI::small);
	# draw a big red line at midnight in the daily graph
	my $vtime = time;
	$vtime = $vtime - ($vtime % abs($start{$CGI::png})) - 3600 * 2;
	push @args, "VRULE:$vtime#cc0000" if $CGI::png eq 'daily';
	# fire up rrdtool
	RRDs::graph(@args);
	my $e = $RRDs::error;
	print_error("Cannot create graph: $e") if $e;
	$e = $RRDs::error if $e; # shut up perl
	# no error, try to send the file
	open(PNG, "<$pngfile") || print_error("Cannot read graph file");
	# ok, send it as image/png
	print $q->header(-type => "image/png", -expires => "$expire{$CGI::png}");
	my $buf;
	# could be sendfile in Linux ;-)
	while(sysread PNG,$buf,4096) {
		print STDOUT $buf;
	}
	close PNG;
} elsif (defined $CGI::log) {
	# show the graphics for one target
	print_error ("Target $CGI::log unknown") if (!exists $targets{$CGI::log});
	my $title;
	# user defined title?
	if ($targets{$CGI::log}{title}) {
		$title = $targets{$CGI::log}{title};
	} else {
		$title = "MRTG/RRD - Target $CGI::log";
	}
	print $q->header, $q->start_html(
		-title => $title,
		-author => 'Rainer.Bawidamann@informatik.uni-ulm.de',
		-bgcolor => $config{background});
	# user defined header line?
	if (exists $targets{$CGI::log}{pagetop}) {
		print $targets{$CGI::log}{pagetop},"\n";
	} else {
		print $q->h1("Target $targets{$CGI::log}{title}"),"\n";
	}
	my $sup = $targets{$CGI::log}{suppress};
	my $url = "$meurl?log=$CGI::log&png";
	# the header lines and tags for the graphics
	if ($sup !~ /d/) {
		print $q->h2("'Daily' graph (5 Minute Average)"),"\n",
			$q->img({src => "$url=daily", alt => "daily-graph"}),
			"\n";
	}
	if ($sup !~ /w/) {
		print $q->h2("'Weekly' graph (30 Minute Average)"),"\n",
			$q->img({src => "$url=weekly", alt => "weekly-graph"}),
			"\n";
	}
	if ($sup !~ /m/) {
		print $q->h2("'Monthly' graph (2 Hour Average)"),"\n",
			$q->img({src => "$url=monthly", alt => "monthly-graph"}),
			"\n";
	}
	if ($sup !~ /y/) {
		print $q->h2("'Yearly' graph (1 Day Average)"),"\n",
			$q->img({src => "$url=yearly", alt => "yearly-graph"}),
			"\n";
	}
	print $footer;
} else {
	# should be unreachable code but ...
	print_error("hae?");
}
exit 0;

# read the mrtg.cfg file
sub read_mrtg_config()
{
	my ($opt, $tar, $val);
	my $line = '';
	my @lines;
	open(CFG, "<$cfgfile") || print_error("Cannot open config file");
	while(<CFG>) {
		chomp;		# remove newline
		s/\s+$//g;	# remove trailing space
		s/\s/ /g;	# collapse white space to one space
		next if /^ *\#/;# ignore comment lines
		next if /^ *$/;	# ignore empty lins
		if (/^ +(.*)$/) {	# continuation lines
			$lines[$#lines] .= " ".$1;
		} else {
			push @lines, $_;
		}
	}
	close CFG;
	# set some defaults
	my %defaults = (
		directory => '',
		suppress => '',
		xsize => 400,
		ysize => 100,
		withpeak => '',
		ylegend => 'Bytes per Second',
		legend1 => 'Incoming Traffic in Bytes per Second',
		legend2 => 'Outgoing Traffic in Bytes per Second',
		legend3 => 'Maximal 5 Minute Incoming Traffic',
		legend4 => 'Maximal 5 Minute Outgoing Traffic',
		kmg => ',k,M,G,T,P'
		);
	%config = (
		writeexpires => 'No',
		background => '#ffffff'
		);
	%{$targets{_}} = %defaults;
	foreach (@lines) {
		if (/^([\d\w]+)\[(\S*)\] *: *(.*)$/) {
			# a target config line
			($tar, $opt, $val) = (lc($2), lc($1), $3);
			$val = '' if !defined $val; # get around undef values
			if (!exists $targets{$tar}{target}) {
				# first occurance of a target, copy defaults
				# (don't need to check for '_' as this exists in any case)
				push @sorted, $tar;
				%{$targets{$tar}} = %{$targets{_}};
			}
			if ($tar eq '_' && $val eq '') {
				# a line "Command[_]:", resets default
				if ($defaults{$opt}) {
					# there is a default for this, set it
					$targets{'_'}{$opt} = $defaults{$opt};
				} else {
					# no default, delete from _
					delete $targets{'_'}{$opt};
				}
			} elsif ($opt eq 'options') {
				# "Option[...]: " - add values to a set of options
				$val = lc($val);
				map {$targets{$tar}{options}{$_} = 1} ($val =~ m/([a-z]+)/g);
			} else {
				# "Command[...]: ..."
				$targets{$tar}{$opt} = $val;
			}
			next;
		} elsif (/^([\d\w]+) *: *(\S*)$/) {
			# global option
			($tar, $opt, $val) = (undef, lc($1), lc($2));
			$config{$opt} = $val;
			next;
		}
		$_ =~ s/</&gt;/g;
		print STDERR localtime()," MRTG/RRD index.cgi: unknown field in mrtg.conf '$_'\n";
	}
	# we need to replace '&nbsp;' in the legends as we print them via rrdtool
	foreach $tar (keys %targets) {
		foreach $opt (qw/legend1 legend2 legend3 legend4 legend5 legendi legendo ylegend shortlegend/) {
			$targets{$tar}{$opt} =~ s'&nbsp;' ' # '
				if exists $targets{$tar}{$opt};
		}
	}
}

sub print_error(@)
{
	print $q->header, $q->start_html(
		-title => 'MRTG/RRD index.cgi - Skript error',
		-author => 'Rainer.Bawidamann@informatik.uni-ulm.de',
		-bgcolor => "#ffffff"),
		$q->h1('Skript Error'),
		@_, $q->end_html;
	exit 0;
}

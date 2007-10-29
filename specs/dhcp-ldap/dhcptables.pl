#!/usr/bin/perl
#
#  dhcptables.pl
#
#  Parse the ISC DHCP common/tables.c to produce a
#  table of currently defined dhcp options as either
#  a C header, a PERL hash, a python dict, or a text file.
#
#  Arguments:
#  
#  <filename> :       alternative location of tables.c - default: ./common/tables.c
#                     If ./common/tables.c does not exist, and no filename is given,
#                     expects tables.c to be on <STDIN> .
#  -c   / --c:        produce C header on stdout (the default)
#  -pe  / --perl:     produce perl hash on stdout
#  -py  / --python:   produce python dict on stdout
#  -d   / --doc:      produce plain text / CSV spreadsheet table on stdout
#
use Getopt::Long;
use IO::Handle;

my($c_header, $perl_hash, $python_dict, $doc_table)=(0,0,0,0);

if ( ! GetOptions('c'     => \$c_header,
		  'perl'  => \$perl_hash,
		  'python'=> \$python_dict,
		  'doc'   => \$doc_table
		  ) 
   )
{
    print "Usage:\n",
'  <filename> :       alternative location of ISC DHCP tables.c - default: ./common/tables.c
                     If ./common/tables.c does not exist, and no filename is given,
                     expects tables.c to be on the standard input .
  -c   / --c:        produce C header on stdout (the default)
  -pe  / --perl:     produce perl hash on stdout
  -py  / --python:   produce python dict on stdout
  -d   / --doc:      produce plain text / CSV spreadsheet table on stdout',
    "\n";
    exit(1);
};

my($tables_c_name) = ($#ARGV > -1) ?  shift(@ARGV) : "common/tables.c";

if( -r $tables_c_name )
{
    close STDIN;
    open(STDIN, '<'.$tables_c_name) || die("Cannot open $tables_c_name: $? $!");
};

$universes={};
while(<>)
{
    if( /^\s*{\s*\"([^\"]+)\"[,\s]*\"([^\"]*)\"[,\s]*&([^_]+)_universe[,\s]*(\d+)/ ) #\s*}[\s\n\r]*$/ )
    {
	if( ! exists ${$universes}{$3} )
	{
	    ${$universes}{$3} = {};
	};
        ${ ${$universes} { $3 } }{ $1 }={ 'type' => $2, 'code' => $4 };
    };
};
if ( $perl_hash )
{
    print '# DHCP Options:
%dhcp_options = (',"\n";
}elsif 
   ( $python_dict )
{
    print '# DHCP Options:
dhcp_options = [',"\n";
}elsif
   ( $doc_table )
{
    print "dhcp_universe_name\tdhcp_option_name\tdhcp_option_code\tdhcp_option_type\n";
}else # $c_header
{
    $c_header = 1;
    print '/* DHCP Options: 
*/
#ifndef DHCP_OPTION_H
#define DHCP_OPTION_H
#ifndef DHCP_OPTION_EXTRA_MEMBER_DECL
#define DHCP_OPTION_EXTRA_MEMBER_DECL
#endif
#ifndef DHCP_OPTION_EXTRA_MEMBER_INITIALIZER
#define DOEMI
#else
#define DOEMI DHCP_OPTION_EXTRA_MEMBER_INITIALIZER
#endif
enum dhcp_universe_code { DHCP_UNIVERSE, NWIP_UNIVERSE, FQDN_UNIVERSE };
struct dhcp_option 
{   unsigned char dhcp_universe_code, 
                  dhcp_option_code;
    unsigned short flags;
    const char   *dhcp_option_name;
    const char   *dhcp_option_format;
    DHCP_OPTION_EXTRA_MEMBER_DECL
} dhcp_options [] =
{',"\n";
}
    
foreach $u ( sort keys %{$universes} )
{
    if ( $perl_hash )
    {
	print "\t'",$u,"',\n\t{\n";
    }
    elsif
       ( $python_dict )
    {
	print "\t'",$u,"' = {", "\n";
    };
    foreach $o ( sort { ${${${$universes}{$u}}{$a}}{'code'} <=> ${${${$universes}{$u}}{$b}}{'code'} } keys %{${$universes}{$u}} )
    {
	if( $o =~ /^unknown-/ )
	{
	    next;
	};
	if ( $c_header )
        {
	    print "\t{ ", 
	          ($u eq 'dhcp') 
		  ? 'DHCP_UNIVERSE'
		  :($u eq 'nwip') 
		  ? 'NWIP_UNIVERSE'
		  :($u eq 'fqdn')
		  ? 'FQDN_UNIVERSE'
		  : 'DHCP_UNIVERSE',
		  ',',"\t",
		  ${${${$universes}{$u}}{$o}}{'code'},
		  ",\t0,\t",'"',
		  $o,
		  '",',"\t\t\t",'"',
		  ${${${$universes}{$u}}{$o}}{'type'},
		  '"', "\tDOEMI ",
		  "},\n";  
	}elsif
	   ( $perl_hash )
        {
	    print "\t\t'",$o,"'",' => { ',"'code'", ' => ', ${${${$universes}{$u}}{$o}}{'code'} ,',',
	                            "\t'type'", ' => ',"'", ${${${$universes}{$u}}{$o}}{'type'} ,"'",
            " },\n";	    
	}elsif
	   ( $python_dict )
        {
	    print "\t\t'",$o,"' : { 'type':'",${${${$universes}{$u}}{$o}}{'type'},"'", 
	                         ", 'code':" ,${${${$universes}{$u}}{$o}}{'code'}," },\n";
	}else
	{
	    print $u,"\t",$o,"\t",${${${$universes}{$u}}{$o}}{'code'}, "\t", ${${${$universes}{$u}}{$o}}{'type'},"\n";
	};
    };
    if( $perl_hash || $python_dict )
    {
	print "\t},\n";
    };
};
if( $perl_hash )
{
    print "\n);\n";
}elsif
  ( $python_dict )
{
    print "\n};\n"
}elsif
  ( $c_header )
{
    print "\n};\n#endif\n";
};

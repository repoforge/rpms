# $Id$
# Authority: dries

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-BarGraph

Summary: Generate ASCII bar graphs
Name: perl-Text-BarGraph
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://www.robobunny.com/projects/bargraph

Source: http://www.robobunny.com/projects/bargraph/Text-BarGraph.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
Text::BarGraph is a simple Perl module for generating ASCII bar graphs based 
on data in a hash, where the keys are labels and the values are magnitudes. 
It automatically scales the graph to fit on your terminal screen. It is very 
useful in making data more meaningful. For example, it can be used with 
statistics gathered from a log file.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
        OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod \
                %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes examples MANIFEST README
%doc %{_mandir}/man?/Text::BarGraph*
%{perl_vendorlib}/Text/BarGraph.pm

%changelog
* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.

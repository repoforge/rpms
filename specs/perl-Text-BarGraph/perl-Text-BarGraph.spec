# $Id$
# Authority: dries

%define perl_vendorlib  %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-BarGraph

Summary: Generate ASCII bar graphs
Name: perl-Text-BarGraph
Version: 1.0
Release: 1.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://www.robobunny.com/projects/bargraph

Source: http://www.cpan.org/modules/by-module/Text/Text-BarGraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::BarGraph is a simple Perl module for generating ASCII bar graphs based
on data in a hash, where the keys are labels and the values are magnitudes.
It automatically scales the graph to fit on your terminal screen. It is very
useful in making data more meaningful. For example, it can be used with
statistics gathered from a log file.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/Text::BarGraph*.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/BarGraph.pm

%changelog
* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.

# $Id$
# Authority: dag
# Upstream: Paul Jamieson Fenwick <pjf$perltraining,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-EverQuest-LogLineParser

Summary: Perl module for parsing lines from the EverQuest log file
Name: perl-Games-EverQuest-LogLineParser
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-EverQuest-LogLineParser/

Source: http://www.cpan.org/modules/by-module/Games/Games-EverQuest-LogLineParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Games-EverQuest-LogLineParser is a Perl module for parsing lines
from the EverQuest log file.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Games/
%dir %{perl_vendorlib}/Games/EverQuest/
%{perl_vendorlib}/Games/EverQuest/eqlog2csv.pl
%{perl_vendorlib}/Games/EverQuest/eqlog_line_type_frequency.pl
%{perl_vendorlib}/Games/EverQuest/eqlog_unrecognized_lines.pl
%{perl_vendorlib}/Games/EverQuest/LogLineParser.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)

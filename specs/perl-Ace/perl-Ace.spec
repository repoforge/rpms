# $Id$
# Authority: dag
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Ace

Summary: Perl module that implements Object-Oriented Access to ACEDB Databases
Name: perl-Ace
Version: 1.91
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AcePerl/

Source: http://www.cpan.org/modules/by-module/Ace/AcePerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Ace is a Perl module that implements Object-Oriented Access
to ACEDB Databases.

%prep
%setup -n %{real_name}Perl-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" <<EOF
1
n
EOF
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog DISCLAIMER.txt MANIFEST META.yml README README.ACEBROWSER install.PLS docs/ examples/
%doc %{_mandir}/man1/ace.pl.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/ace.pl
%{perl_vendorlib}/Ace/
%{perl_vendorlib}/Ace.pm
%{perl_vendorlib}/GFF/
%{perl_vendorlib}/auto/Ace/
%{perl_vendorarch}/auto/Ace/

%changelog
* Sat Oct 06 2007 Dag Wieers <dag@wieers.com> - 1.91-1
- Initial package. (using DAR)

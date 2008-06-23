# $Id$
# Authority: dag
# Upstream: Theo Schlossnagle <jesus$omniti,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spread
%define real_version 3.17.3-1.07

Summary: Perl extension for the Spread group communication system
Name: perl-Spread
Version: 3.17.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spread/

Source: http://www.cpan.org/authors/id/J/JE/JESUS/Spread-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libspread-devel
BuildRequires: perl

%description
Perl extension for the Spread group communication system.

%prep
%setup -n %{real_name}-%{real_version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/Spread.3pm*
%{perl_vendorarch}/auto/Spread/
%{perl_vendorarch}/Spread.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 3.17.3-1
- Initial package. (using DAR)

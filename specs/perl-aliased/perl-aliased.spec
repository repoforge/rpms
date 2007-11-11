# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name aliased

Summary: aliased module for perl
Name: perl-aliased
Version: 0.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/aliased/

Source: http://www.cpan.org/modules/by-module/aliased/aliased-%{version}.tar.gz
#Source: http://www.cpan.org/authors/id/O/OV/OVID/aliased-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl

%description
aliased module for perl.

%prep
%setup -n %{real_name}-%{version}

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
%doc ANNOUNCE ChangeLog Changes LICENSE MANIFEST README TODO
%doc %{_mandir}/man3/aliased.3pm*
%{perl_vendorarch}/aliased.pm
%{perl_vendorarch}/auto/aliased/

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)

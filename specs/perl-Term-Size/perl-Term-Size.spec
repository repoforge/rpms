# $Id$
# Authority: dag
# Upstream: Tim Goodwin <tjg$star,le,ac,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Size

Summary: Perl extension for retrieving terminal size
Name: perl-Term-Size
Version: 0.2
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Size/

Source: http://www.cpan.org/modules/by-module/Term/Term-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl extension for retrieving terminal size.

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
%doc Changes Copyright INSTALL MANIFEST README
%doc %{_mandir}/man3/Term::Size.3pm*
%dir %{perl_vendorarch}/auto/Term/
%{perl_vendorarch}/auto/Term/Size/
%dir %{perl_vendorarch}/Term/
%{perl_vendorarch}/Term/Size.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)

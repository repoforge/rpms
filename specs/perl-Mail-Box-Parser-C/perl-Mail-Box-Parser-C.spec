# $Id$
# Authority: dag
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-Box-Parser-C

Summary: Perl module for parsing folders for MailBox with C routines
Name: perl-Mail-Box-Parser-C
Version: 3.006
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-Box-Parser-C/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-Box-Parser-C-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Mail-Box-Parser-C is a Perl module for parsing folders for MailBox
with C routines.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Mail::Box::Parser::C.3pm*
%dir %{perl_vendorarch}/Mail/
%dir %{perl_vendorarch}/Mail/Box/
%dir %{perl_vendorarch}/Mail/Box/Parser/
%{perl_vendorarch}/Mail/Box/Parser/C.pm
%dir %{perl_vendorarch}/auto/Mail/
%dir %{perl_vendorarch}/auto/Mail/Box/
%dir %{perl_vendorarch}/auto/Mail/Box/Parser/
%{perl_vendorarch}/auto/Mail/Box/Parser/C/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 3.006-1
- Initial package. (using DAR)

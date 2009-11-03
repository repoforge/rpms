# $Id$
# Authority: dag
# Upstream: Charles Ying <cying$photonfx,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sendmail-Milter

Summary: Perl module to interface with sendmail's Mail Filter API
Name: perl-Sendmail-Milter
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sendmail-Milter/

Source: http://www.cpan.org/modules/by-module/Sendmail/Sendmail-Milter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: sendmail-devel

%description
perl-Sendmail-Milter is a Perl module.

This package contains the following Perl module:

    Sendmail::Milter

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
%doc Changes LICENSE MANIFEST README TODO
%doc %{_mandir}/man3/Sendmail::Milter.3pm*
%dir %{perl_vendorarch}/Sendmail/
%{perl_vendorarch}/Sendmail/Milter.pm
%{perl_vendorarch}/Sendmail/sample.pl
%dir %{perl_vendorarch}/auto/Sendmail/
%{perl_vendorarch}/auto/Sendmail/Milter/

%changelog
* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)

# $Id: perl-Text-Iconv 201 2004-06-03 15:24:49Z bert $
# Authority: dag
# Upstream: Michael Piotrowski <mxp$dynalabs,de>

### EL6 ships with perl-Text-Iconv-1.7-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Iconv

Summary: Text::Iconv perl module
Name: perl-Text-Iconv
Version: 1.7
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Iconv/

Source: http://www.cpan.org/modules/by-module/Text/Text-Iconv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Perl interface to the iconv() codeset conversion function, as
defined by the Single UNIX Specification.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Iconv.3pm*
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Iconv/
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Iconv.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Sun Feb 20 2005 Dag Wieers <dag@wieers.com> - 1.4-1
- Improved %%files list.

* Fri May 21 2004 Dag Wieers <dag@wieers.com> - 1.2-0
- Cosmetic cleanup.

* Tue Apr 06 2004 Bert de Bruijn <bert@debruijn.be>
- initial spec (adapted from PLD).


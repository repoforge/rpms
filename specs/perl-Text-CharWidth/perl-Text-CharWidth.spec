# $Id$
# Authority: dag
# Upstream: ??? ?? <kubota$debian,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CharWidth

Summary: Perl module to get number of occupied columns of a string on terminal
Name: perl-Text-CharWidth
Version: 0.04
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CharWidth/

Source: http://www.cpan.org/modules/by-module/Text/Text-CharWidth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Text-CharWidth is a Perl module to get number of occupied columns
of a string on terminal.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Text::CharWidth.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/CharWidth.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/CharWidth/

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)

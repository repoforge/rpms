# $Id$
# Authority: dag
# Upstream: Kellan Elliott-Mccrea <kellan$protest,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-W3CDTF

Summary: Perl module to parse and format W3CDTF datetime strings
Name: perl-DateTime-Format-W3CDTF
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-W3CDTF/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-W3CDTF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
DateTime-Format-W3CDTF is a Perl module to parse and format
W3CDTF datetime strings.

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/DateTime::Format::W3CDTF.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/W3CDTF.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)

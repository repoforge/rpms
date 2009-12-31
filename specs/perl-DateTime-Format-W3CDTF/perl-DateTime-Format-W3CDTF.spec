# $Id$
# Authority: dag
# Upstream: Kellan Elliott-Mccrea <kellan$protest,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-W3CDTF

Summary: Perl module to parse and format W3CDTF datetime strings
Name: perl-DateTime-Format-W3CDTF
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-W3CDTF/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-Format-W3CDTF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(DateTime)
BuildRequires: perl(Test::More)
Requires: perl(DateTime)

%filter_from_requires /^perl*/d
%filter_setup


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
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.05-1
- Updated to version 0.05.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)

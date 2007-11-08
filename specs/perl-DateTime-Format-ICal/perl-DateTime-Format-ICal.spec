# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-ICal

Summary: Perl module to parse and format iCal datetime and duration strings
Name: perl-DateTime-Format-ICal
Version: 0.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-ICal/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-ICal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)(Module::Build)
Requires: perl

%description
DateTime-Format-ICal is a Perl module to parse and format
iCal datetime and duration strings.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/DateTime::Format::ICal.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/ICal.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)

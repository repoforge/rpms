# $Id$
# Authority: dag
# Upstream: Dave Rolsky <autarch$urth,org>
# Upstream: Flavio Soibelmann Glock <fglock$pucrs,br>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-ICal

Summary: Parse and format iCal datetime and duration strings
Name: perl-DateTime-Format-ICal
Version: 0.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-ICal/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Format-ICal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Build)

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
%doc Changes LICENSE MANIFEST META.yml TODO
%doc %{_mandir}/man3/DateTime::Format::ICal.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Format/
%{perl_vendorlib}/DateTime/Format/ICal.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)

# $Id$
# Authority: dries
# Upstream: Jaldhar H, Vyas <jaldhar$braincells,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Calendar-Discordian
%define real_version 0.009006

Summary: Perl extension for the Discordian Calendar
Name: perl-DateTime-Calendar-Discordian
Version: 0.9.6
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Calendar-Discordian/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Calendar-Discordian-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a module that implements the Discordian calendar made popular
in the "Illuminatus!" trilogy by Robert Shea and Robert Anton Wilson and
by the Church of the SubGenius.  It follows the DateTime API.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/DateTime::Calendar::Discordian.3pm*
%dir %{perl_vendorlib}/DateTime/
%dir %{perl_vendorlib}/DateTime/Calendar/
%{perl_vendorlib}/DateTime/Calendar/Discordian.pm

%changelog
* Wed Mar 12 2008 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release

* Thu Mar 06 2008 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Initial package.

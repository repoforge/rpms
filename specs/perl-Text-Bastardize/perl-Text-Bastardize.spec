# $Id$
# Authority: dries
# Upstream: Julian Fondren <ayrnieu$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Bastardize

Summary: Corruptor of innocent text
Name: perl-Text-Bastardize
Version: 0.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Bastardize/

Source: http://www.cpan.org/modules/by-module/Text/Text-Bastardize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A corruptor of innocent text.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::Bastardize.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Bastardize/
%{perl_vendorlib}/Text/Bastardize.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.

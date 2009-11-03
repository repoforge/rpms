# $Id$
# Authority: dries
# Upstream: Benjamin Franz <snowhare$nihongo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Stem

Summary: Stemming of words
Name: perl-Lingua-Stem
Version: 0.83
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Stem/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Stem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Provides word stemming algorithms localized by language.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Artistic_License.txt Changes GPL_License.txt LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Lingua::Stem.3pm*
%doc %{_mandir}/man3/Lingua::Stem::*.3pm*
%dir %{perl_vendorlib}/Lingua/
%{perl_vendorlib}/Lingua/Stem/
%{perl_vendorlib}/Lingua/Stem.pm
%{perl_vendorlib}/Lingua/Stem.pod
%{perl_vendorlib}/Lingua/test.pl

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.83-1
- Updated to release 0.83.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Initial package.

# $Id$
# Authority: dries
# Upstream: Kim Rutherford <cpan$xenu,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Same

Summary: Look for similarities between files or arrays
Name: perl-Text-Same
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Same/

Source: http://www.cpan.org/modules/by-module/Text/Text-Same-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Look for similarities between files or arrays.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man1/psame.1*
%doc %{_mandir}/man3/Text::Same.3pm*
%doc %{_mandir}/man3/Text::Same::*.3pm*
%{_bindir}/psame
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Same/
%{perl_vendorlib}/Text/Same.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.

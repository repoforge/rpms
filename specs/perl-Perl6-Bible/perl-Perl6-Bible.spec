# $Id$
# Authority: dag
# Upstream: ☺唐鳳☻ <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Perl6-Bible

Summary: Perl 6 Design Documentations
Name: perl-Perl6-Bible
Version: 0.37
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Perl6-Bible/

Source: http://www.cpan.org/modules/by-module/Perl6/Perl6-Bible-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.0

%description
Perl 6 Design Documentations.

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
%doc %{_mandir}/man3/Perl6::Bible.3pm*
%{_bindir}/p6bible
%dir %{perl_vendorlib}/Perl6/
%{perl_vendorlib}/Perl6/Bible.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.37-1
- Updated to release 0.37.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.30-1
- Initial package. (using DAR)

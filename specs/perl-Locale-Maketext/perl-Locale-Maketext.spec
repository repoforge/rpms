# $Id$
# Authority: dag
# ExclusiveDist: rh6 el2 rh7

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext

Summary: framework for localization and inheritance-based lexicons for Perl
Name: perl-Locale-Maketext
Version: 1.09
Release: 1.2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Maketext-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

%description
Locale::Maketext is a base class providing a framework for
localization and inheritance-based lexicons, as described in my
article in The Perl Journal #13 (a corrected version of which appears
in this dist).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Locale/
%{perl_vendorlib}/Locale/Maketext/
%{perl_vendorlib}/Locale/Maketext.pm
%{perl_vendorlib}/Locale/Maketext.pod

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.09-1.2
- Rebuild for Fedora Core 5.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 1.06-1
- Cosmetic cleanup.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.06-0
- Updated to release 1.06.

* Sat Feb 01 2003 Dag Wieers <dag@wieers.com> - 1.03-0
- Initial package. (using DAR)

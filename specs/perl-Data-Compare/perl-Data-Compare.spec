# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Compare

Summary: Compare perl data structures
Name: perl-Data-Compare
Version: 1.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Compare/

Source: http://www.cpan.org/modules/by-module/Data/Data-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module compares arbitrary data structures to see if they are copies
of each other.

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
%doc CHANGES MANIFEST META.yml NOTES README TODO
%doc %{_mandir}/man3/Data::Compare.3pm*
%doc %{_mandir}/man3/Data::Compare::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Compare/
%{perl_vendorlib}/Data/Compare.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.18-1
- Updated to release 1.18.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Updated to release 0.16.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Initial package.


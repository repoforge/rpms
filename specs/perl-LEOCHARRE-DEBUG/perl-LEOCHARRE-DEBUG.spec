# $Id$
# Authority: dag
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name LEOCHARRE-DEBUG

Summary: Leo Charre's default debug subroutines
Name: perl-LEOCHARRE-DEBUG
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/LEOCHARRE-DEBUG/

Source: http://www.cpan.org/authors/id/L/LE/LEOCHARRE/LEOCHARRE-DEBUG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Leo Charre's default debug subroutines.

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/LEOCHARRE::DEBUG.3pm*
%dir %{perl_vendorlib}/LEOCHARRE/
#%{perl_vendorlib}/LEOCHARRE/DEBUG/
%{perl_vendorlib}/LEOCHARRE/DEBUG.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)

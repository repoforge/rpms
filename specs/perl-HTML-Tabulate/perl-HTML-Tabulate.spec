# $Id$
# Authority: dag
# Upstream: Gavin Carr <gavin$openfusion,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tabulate

Summary: HTML table rendering class
Name: perl-HTML-Tabulate
Version: 0.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tabulate/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Tabulate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
HTML table rendering class.

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
%doc MANIFEST README
%doc %{_mandir}/man3/HTML::Tabulate.3pm*
%dir %{perl_vendorlib}/HTML/
#%{perl_vendorlib}/HTML/Tabulate/
%{perl_vendorlib}/HTML/Tabulate.pm

%changelog
* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Initial package. (using DAR)

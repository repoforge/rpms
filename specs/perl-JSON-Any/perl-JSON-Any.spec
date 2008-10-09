# $Id$
# Authority: dag
# Upstream: Chris Thompson <cthom$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-Any

Summary: Wrapper Class for the various JSON classes
Name: perl-JSON-Any
Version: 1.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-Any/

Source: http://www.cpan.org/modules/by-module/JSON/JSON-Any-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(JSON)
BuildRequires: perl(JSON::DWIW)
BuildRequires: perl(JSON::PC)
BuildRequires: perl(JSON::Syck)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Test::More)

%description
Wrapper Class for the various JSON classes.

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
%doc %{_mandir}/man3/JSON::Any.3pm*
%dir %{perl_vendorlib}/JSON/
#%{perl_vendorlib}/JSON/Any/
%{perl_vendorlib}/JSON/Any.pm

%changelog
* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 1.17-1
- Updated to release 1.17.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)

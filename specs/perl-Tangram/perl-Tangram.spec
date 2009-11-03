# $Id$
# Authority: dag
# Upstream: Sam Vilain <sam$vilain,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tangram

Summary: Store pure objects in standard relational databases
Name: perl-Tangram
Version: 2.10
Release: 2%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tangram/

Source: http://www.cpan.org/modules/by-module/Tangram/Tangram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

### Provides required by package itself
Provides: perl(Tangram::Compat::Stub)

%description
Store pure objects in standard relational databases.

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
%doc COPYING Changes.pod MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Tangram.3pm*
%doc %{_mandir}/man3/Tangram::*.3pm*
%{perl_vendorlib}/auto/Tangram/
%{perl_vendorlib}/Tangram/
%{perl_vendorlib}/Tangram.pm
%{perl_vendorlib}/Tangram.pod

%changelog
* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 2.10-2
- Added selfcontained provides.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 2.10-1
- Updated to release 2.10.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.09-1
- Initial package. (using DAR)

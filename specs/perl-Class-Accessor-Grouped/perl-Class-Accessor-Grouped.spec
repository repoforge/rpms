# $Id$
# Authority: dag
# Upstream: Matt S. Trout <mst$shadowcatsystems,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Grouped

Summary: Lets you build groups of accessors
Name: perl-Class-Accessor-Grouped
Version: 0.09000
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Grouped/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-Grouped-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name) >= 0.04
BuildRequires: perl(Sub::Identify)
Requires: perl >= 1:5.6.1

%description
Lets you build groups of accessors.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Class::Accessor::Grouped.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
#%{perl_vendorlib}/Class/Accessor/Grouped/
%{perl_vendorlib}/Class/Accessor/Grouped.pm

%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.09000-1
- Updated to version 0.09000.

* Wed May 13 2009 Dag Wieers <dag@wieers.com> - 0.08003-1
- Updated to release 0.08003.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 0.08002-1
- Updated to release 0.08002.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.08001-1
- Updated to release 0.08001.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.07000-1
- Initial package. (using DAR)

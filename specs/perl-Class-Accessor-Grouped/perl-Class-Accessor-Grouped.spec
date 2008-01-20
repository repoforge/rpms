# $Id$
# Authority: dag
# Upstream: Matt S. Trout <mst@shadowcatsystems.co.uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Grouped

Summary: Lets you build groups of accessors
Name: perl-Class-Accessor-Grouped
Version: 0.07000
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Grouped/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-Grouped-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Class::Inspector)
Requires: perl >= 1:5.6.1

%description
Lets you build groups of accessors.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Class::Accessor::Grouped.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Accessor/
#%{perl_vendorlib}/Class/Accessor/Grouped/
%{perl_vendorlib}/Class/Accessor/Grouped.pm

%changelog
* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.07000-1
- Initial package. (using DAR)

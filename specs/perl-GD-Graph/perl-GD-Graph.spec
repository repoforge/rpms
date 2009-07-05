# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GDGraph

Summary: Graph plotting module for Perl
Name: perl-GD-Graph
Version: 1.44
Release: 1
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GDGraph/

Source: http://www.cpan.org/modules/by-module/GD/GDGraph-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/GDGraph/GDGraph-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
Graph plotting module for Perl.

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/GD/
%{perl_vendorlib}/GD/Graph/
%{perl_vendorlib}/GD/Graph.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 1.44-1
- Updated to version 1.44.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.43-1.2
- Rebuild for Fedora Core 5.

* Sat Apr 02 2005 Dag Wieers <dag@wieers.com> - 1.43-1
- Cosmetic cleanup.
- Fixed BuildArch, now noarch.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 1.43-0
- Initial package. (using DAR)

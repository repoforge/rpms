# $Id$
# Authority: dries
# Upstream: Jeremy Wadsack <dgsupport$wadsack-allen,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name GD-Graph3d

Summary: Create 3D Graphs
Name: perl-GD-Graph3d
Version: 0.63
Release: 2.2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GD-Graph3d/

Source: http://www.cpan.org/modules/by-module/GD/GD-Graph3d-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(GD)
BuildRequires: perl(GD::Text)
BuildRequires: perl(GD::Graph)
BuildRequires: perl(ExtUtils::MakeMaker)

### Obsolete to provide fedora.us compatibility
Obsoletes: perl-GDGraph3d <= %{version}

%description
With this perl module, you can create 3D graphs with GD.

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
%doc Changes
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/GD/
%{perl_vendorlib}/GD/Graph3d.pm
%dir %{perl_vendorlib}/GD/Graph/
%{perl_vendorlib}/GD/Graph/*.pm

%changelog
* Sun Oct 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.63-2
- Rebuild.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.63-1
- Initial package.

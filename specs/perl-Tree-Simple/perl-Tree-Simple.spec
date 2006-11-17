# $Id$
# Authority: dries
# Upstream: Stevan Little <stevan$iinteractive,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tree-Simple

Summary: Simple tree object
Name: perl-Tree-Simple
Version: 1.17
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tree-Simple/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STEVAN/Tree-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A simple tree object.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Tree/Simple.pm
%{perl_vendorlib}/Tree/Simple/

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Initial package.

# $Id$
# Authority: dries
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Find-Rule

Summary: Alternative interface to File::Find
Name: perl-File-Find-Rule
Version: 0.30
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Find-Rule/

Source: http://www.cpan.org/modules/by-module/File/File-Find-Rule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module contains an alternative interface to File::Find.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/findrule
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Find/
%{perl_vendorlib}/File/Find/Rule.pm
%{perl_vendorlib}/File/Find/Rule/*.pod

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.28-1.2
- Rebuild for Fedora Core 5.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.

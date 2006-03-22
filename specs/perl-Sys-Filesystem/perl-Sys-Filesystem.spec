# $Id$
# Authority: dries
# Upstream: Nicola Worthington <nicolaw$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sys-Filesystem

Summary: Interface to filesystem names and their properties
Name: perl-Sys-Filesystem
Version: 1.18
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sys-Filesystem/

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NICOLAW/Sys-Filesystem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Sys::Filesystem is intended to be a portable interface to list and
query filesystem names and their properties.

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
%{perl_vendorlib}/Sys/Filesystem.pm
%{perl_vendorlib}/Sys/Filesystem/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.

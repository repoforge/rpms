# $Id$
# Authority: dries
# Upstream: Michael Accardo <mikeaccardo$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name PHP-Perlinfo

Summary: Clone of PHP's phpinfo function for Perl
Name: perl-PHP-Perlinfo
Version: 0.08
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PHP-Perlinfo/

Source: http://www.cpan.org/modules/by-module/PHP/PHP-Perlinfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(PHP::Perlinfo::HTML) = %{version}-%{release}

%description
This module outputs a large amount of information (only in HTML in this
release) about the current state of Perl. So far, this includes information 
about Perl compilation options, the Perl version, server information and 
environment, OS version information, Perl modules, and the Perl License.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/PHP/
%{perl_vendorlib}/PHP/Perlinfo.pm
%{perl_vendorlib}/PHP/Perlinfo/

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.07-2
- Added perl(PHP::Perlinfo::HTML) provides.

* Fri Mar 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Updated to release 0.07.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.

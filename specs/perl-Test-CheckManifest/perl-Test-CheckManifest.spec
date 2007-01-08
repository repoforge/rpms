# $Id$
# Authority: dries
# Upstream: Renee Baecker <module$renee-baecker,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-CheckManifest

Summary: Checks manifest files
Name: perl-Test-CheckManifest
Version: 1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-CheckManifest/

Source: http://search.cpan.org//CPAN/authors/id/R/RE/RENEEB/Test-CheckManifest-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Checks manifest files.

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
%doc %{_mandir}/man3/Test::CheckManifest*
%{perl_vendorlib}/Test/CheckManifest.pm

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Updated to release 1.0.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.

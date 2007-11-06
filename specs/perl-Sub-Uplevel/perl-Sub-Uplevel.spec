# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Uplevel

Summary: Apparently run a function in a higher stack frame
Name: perl-Sub-Uplevel
Version: 0.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Uplevel/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/Sub-Uplevel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Apparently run a function in a higher stack frame.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Sub/Uplevel.pm

%changelog
* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.13-1
- Updated to release 0.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.

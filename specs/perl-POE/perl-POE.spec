# $Id$
# Authority: dries
# Upstream: Rocco Caputo <rcaputo$pobox,com>

# ExcludeDist: el3

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE

Summary: Portable multitasking and networking framework for Perl
Name: perl-POE
Version: 0.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE/

Source: http://search.cpan.org/CPAN/authors/id/R/RC/RCAPUTO/POE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Provides: perl(POE::Resource::Controls)

%description
POE is a networking and multitasking (some say cooperative threading)
framework for Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	--default \
	PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES HISTORY README TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/POE/
%{perl_vendorlib}/POE.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1
Updated to release 0.38.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.3202-1
- Updated to release 0.3202.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.3101-1
- Updated to release 0.3101.

* Thu Apr 28 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.3009-1
- Updated to release 0.3009.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.3003-1
- Initial package.

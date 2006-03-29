# $Id$
# Authority: dries
# Upstream: Franco Callari <franco$cim,mcgill,ca>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Resources

Summary: Handling application defaults
Name: perl-Resources
Version: 1.04
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Resources/

Source: http://search.cpan.org/CPAN/authors/id/F/FR/FRANCOC/Resources-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Resources.pm is Perl package used to specify configuration (defaults, ...)
parameters for Perl applications, pretty much in the same way as XWindows
does.  It implements dynamical inheritance of defaults (both values and names)
through subclassing, parameter loading from files, runtime parameter viewing
and editing. The package contains an extensive documentation in POD format, to
which you are kindly referred.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Resources.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
